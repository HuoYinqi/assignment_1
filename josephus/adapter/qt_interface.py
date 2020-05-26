from PyQt5 import QtWidgets

from josephus.interface.interface import Interface
from josephus.adapter.txt_reader import TxtReader
from josephus.adapter.csv_reader import CSVReader
from josephus.adapter.qt_interface_without_function import Ui_MainWindow
from josephus.domain.person import Person
from josephus.use_cases.josephus import Josephus

class JosephusWindow(Interface, QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(JosephusWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Josephus') 

        self.button_file.clicked.connect(self.create_and_show_reader)
        self.line_edit_start.textChanged.connect(self.set_start_value_)
        self.line_edit_step.textChanged.connect(self.set_step_value_)       
        self.button_ok.clicked.connect(self.create_josephus_)

        self.button_next.clicked.connect(self.next_)
        self.button_run.clicked.connect(self.run)
        self.button_clear.clicked.connect(self.clear)
        self.button_quit.clicked.connect(self.quit)

    def create_and_show_reader(self):
        target_file: str = ''
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open file',
            'data',
            '*.txt *.csv *.zip'
        )
        filenames = self.get_namelist_from_zip(filepath)       
        if filenames:
            content = 'please select file:\n'
            for each in filenames:
                content = content + each + '\n'

            target_file, ok = QtWidgets.QInputDialog.getText(self, 'select file in zip', content)
            if not ok:
                self.create_and_show_reader()
                return
        try:
            self.create_reader(filepath, target_file)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(self, 'Warning','please input correct filename' )

        self.people_info.setText(self.get_people_info(self.reader))

    def create_josephus_(self):
        content = self.people_info.toPlainText().strip()
        if not content:
            return
        try:
            self.create_josephus(content)
        except:
            self.message_box_warning_text_format()
            return

        self.people_info.setText(self.get_people_info(self.josephus.people))
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
                f'The value of start range from 1 to {len(self.josephus)} '
            )

    def next_(self):
        try:
            some_one = next(self.josephus)
            self.result.append(f'{some_one.name}, {some_one.age}')
        except StopIteration:
            self.result.append("That's all")
        except AttributeError:
            pass

    def run(self):
        try:
            self.result.setText(self.get_result())
        except AttributeError:
            pass

    def quit(self):
        QtWidgets.QApplication.exit()   
        
    def clear(self):
        self.result.clear()
