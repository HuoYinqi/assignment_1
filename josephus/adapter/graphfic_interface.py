import sys
import zipfile
from PyQt5 import QtWidgets

from josephus.interface.interface import Interface
from josephus.adapter.txt_reader import TxtReader
from josephus.adapter.csv_reader import CSVReader
from josephus.interface.josephus_interface import Ui_MainWindow
from josephus.domain.person import Person
from josephus.use_cases.josephus import Josephus

class JosephusWindow(Interface, QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(JosephusWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Josephus') 

        self.toolButton_file.clicked.connect(self.create_josephus_from_reader)
        self.lineEdit_start.textChanged.connect(self.set_start_value_)
        self.lineEdit_step.textChanged.connect(self.set_step_value_)       
        self.toolButton_ok.clicked.connect(self.create_josephus_)

        self.toolButton_next.clicked.connect(self.next_)
        self.toolButton_run.clicked.connect(self.run)
        self.toolButton_clear.clicked.connect(self.clear)
        self.toolButton_quit.clicked.connect(self.quit)

    def create_josephus_from_reader(self):
        target_file: str = ''
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open file',
            'data',
            '*.txt *.csv *.zip'
        )

        if not filepath:
            return         
        
        elif '.zip' in filepath:
            with zipfile.ZipFile(filepath) as zip_file:
                filenames = zip_file.namelist()
                content = 'please select file:\n'
                for each in filenames:
                    content = content + each + '\n'
                
                target_file, ok = QtWidgets.QInputDialog.getText(self, 'select file in zip', content)
                if not ok:
                    self.create_josephus_from_reader()
                    return
        try:
            self.create_reader(filepath, target_file)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(self, 'Warning','please input correct filename' )

        self.create_josephus()
        self.textEdit.setText(self.get_people_info())
        try:
            self.check_strat_value()
        except ValueError:
            self.message_box_warning_start_value()
        
    def create_josephus_(self):
        self.create_josephus()
        content = self.textEdit.toPlainText().strip()
        if content:
            person_info = content.split('\n')
            for item in person_info:
                info = item.split(',')
                name = info[0]
                try:
                    age = int(info[1])
                except ValueError:
                    age = 0
                except IndexError:
                    self.message_box_warning_text_format()
                    return
                self.josephus.append(Person(name, age))  

        self.textEdit.setText(self.get_people_info())
        try:
            self.check_strat_value()
        except ValueError:
            self.message_box_warning_start_value()


    def set_start_value_(self, start):
        try:
            self.set_start_value(start)
            self.label_hint_start.setText('')
        except ValueError:
            self.set_start_value(1)
            self.hint_start_value()
       
    def hint_start_value(self):
        self.label_hint_start.setText('please input an integer more than 0')

    def set_step_value_(self, step):
        try:
            self.set_step_value(step)
            self.label_hint_step.setText('')
        except ValueError:
            self.set_step_value(1)
            self.hint_step_value()

    def hint_step_value(self):
        self.label_hint_step.setText('please input an integer more than 0')
       
    def message_box_warning_text_format(self):
        QtWidgets.QMessageBox.information(
                self,
                'Warning',
                'please input correct format in the text box\nfor example: Bob, 12'
            )

    def message_box_warning_start_value(self):
        QtWidgets.QMessageBox.information(
                self,
                'Warning',
                f'The value of start range from 1 to {len(self.josephus.people)} '
            )

    def next_(self):
        try:
            some_one = next(self.josephus)
            self.textBrowser.append(f'{some_one.name}, {some_one.age}')
        except StopIteration:
            self.textBrowser.append("That's all")
        except AttributeError:
            pass

    def run(self):
        try:
            self.textBrowser.setText(self.get_result())
        except AttributeError:
            pass

    def quit(self):
        QtWidgets.QApplication.exit()   
        
    def clear(self):
        self.textBrowser.clear()