import sys
import zipfile

from PyQt5 import QtWidgets


from josephus.reader.txt_reader import TxtReader
from josephus.reader.csv_reader import CSVReader
from josephus_interface import Ui_MainWindow
from josephus.domain.person import Person
from josephus.use_cases.josephus import Josephus

class Josephus_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Josephus_Window, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Josephus')
        self.reader = None
        self.start = 1
        self.step = 1
        
        
        self.toolButton_file.clicked.connect(self.get_file)
        self.lineEdit_start.textChanged.connect(self.set_start_value)
        self.lineEdit_step.textChanged.connect(self.set_step_value)
        
        self.toolButton_ok.clicked.connect(self.create_josephus)
        self.toolButton_next.clicked.connect(self.next_)
        self.toolButton_run.clicked.connect(self.run)
        self.toolButton_clear.clicked.connect(self.clear)
        self.toolButton_quit.clicked.connect(self.quit)

    def get_file(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open file',
            'D:\\软件培训\\库',
            '*.txt *.csv *.zip'
        )

        if filepath:
            if '.txt' in filepath:
                self.reader = TxtReader(filepath)

            elif '.csv' in filepath:
                self.reader = CSVReader(filepath)

            elif '.zip' in filepath:
                with zipfile.ZipFile(filepath) as zip_file:
                    filenames = zip_file.namelist()
                    content = 'please select file:\n'
                    for each in filenames:
                        content = content + each + '\n'
                    
                    target_file, ok = QtWidgets.QInputDialog.getText(self, 'select file in zip', content)

                    while target_file not in filenames and ok:
                        QtWidgets.QMessageBox.information(self, 'Warning', 'please input correct filename!')
                        target_file, ok = QtWidgets.QInputDialog.getText(self, 'select file in zip', content)

                    if ok:
                        if '.txt' in target_file:
                            self.reader = TxtReader.from_zip(filepath, target_file)
                            filepath = zip_file.extract(target_file, 'data')
                        
                        elif '.csv' in target_file:
                            self.reader = CSVReader.from_zip(filepath, target_file)
                            filepath = zip_file.extract(target_file, 'data')
                    else:
                        self.get_file()
                        return
                
            with open(filepath) as target_file:
                content = target_file.read()
                self.textEdit.setText(content)      


    def set_start_value(self, start):
        try:
            self.start = int(start)
            self.label_hint_start.setText('')
        except ValueError:
            self.start = 0
            self.hint_start_value()
    
    def hint_start_value(self):
        self.label_hint_start.setText('please input an integer')

    def set_step_value(self, step):
        try:
            self.step = int(step)
            self.label_hint_step.setText('')
        except ValueError:
            self.step = 0
            self.hint_step_value()

    def hint_step_value(self):
        self.label_hint_step.setText('please input an integer')

    def create_josephus(self):
        if not self.textEdit.toPlainText():
            QtWidgets.QMessageBox.information(self, 'Warning', 'People can not be none')
            return

        self.josephus = Josephus(reader=self.reader)
        self.josephus.start = self.start
        self.josephus.step = self.step
        if not self.reader:   
            content = self.textEdit.toPlainText()
            if content:
                person_info = content.split('\n')
                for item in person_info:
                    temp = item.split(',')
                    name = temp[0]
                    try:
                        age = int(temp[1])
                    except ValueError:
                        age = 0
                    except IndexError:
                        self.message_box_warning_text_format()
                        return
                    self.josephus.append(Person(name, age))

        self.reader = None

        if self.josephus.start < 1 or self.josephus.start > len(self.josephus.people):
            self.message_box_warning_start_value()
            
        elif self.josephus.step < 1:
            self.message_box_warning_step_value()
        

    def message_box_warning_text_format(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Information)
        message_box.setWindowTitle('Warning')
        message_box.setText(f'please input correct format in the text box\nfor example: Bob, 12')
        message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        message_box.exec()


    def message_box_warning_start_value(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Information)
        message_box.setWindowTitle('Warning')
        message_box.setText(f'The value of start range from 1 to {len(self.josephus.people)} ')
        message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        message_box.exec()

    def message_box_warning_step_value(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Information)
        message_box.setWindowTitle('Warning')
        message_box.setText('The value of step should be more than 0 ')
        message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        message_box.exec()


    def next_(self):
        try:
            some_one = next(self.josephus)
            self.textBrowser.append(f'{some_one.name}, {some_one.age}')
        except StopIteration:
            self.textBrowser.append("That's all")


    def run(self):
        self.textBrowser.setText('')
        result = self.josephus.query_list()
        length = len(result)
        count = 1
        for each in result:
            if count < length:
                self.textBrowser.append(f'elimination\t\t{each.name}, {each.age}')
            else:
                self.textBrowser.append(f'winner\t\t{each.name}, {each.age}')
            count += 1

    def quit(self):
        QtWidgets.QApplication.exit()   
        
    def clear(self):
        self.textBrowser.clear()
        self.create_josephus()

            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Josephus_Window()
    window.show()
    sys.exit(app.exec_())