import sys

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

        self.reader = None
        self.toolButton_file.clicked.connect(self.get_file)
        self.josephus = Josephus(self.reader)
        self.lineEdit_start.textChanged.connect(self.set_start_value)
        self.lineEdit_step.textChanged.connect(self.set_step_value)
        
        self.toolButton_ok.clicked.connect(self.load_people)
        self.toolButton_run.clicked.connect(self.run)
        self.toolButton_quit.clicked.connect(self.quit)

    def get_file(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        file_dialog.setNameFilter('*.txt *.csv')

        if file_dialog.exec_():
            filepaths = file_dialog.selectedFiles()
            filepath = filepaths[0]
            with open(filepath) as target_file:
                content = target_file.read()
                self.textEdit.setText(content)         

    def set_start_value(self, start):
        self.josephus.start = int(start)

    def set_step_value(self, step):
        self.josephus.step = int(step)

    def load_people(self):
        self.josephus.people = []
        content = self.textEdit.toPlainText()
        person_info = content.split('\n')
        for item in person_info:
            temp = item.split(',')
            name = temp[0]
            age = int(temp[1])
            self.josephus.append(Person(name, age))

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
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Josephus_Window()
    window.show()
    sys.exit(app.exec_())