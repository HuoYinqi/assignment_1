import zipfile

from josephus.interface.interface import Interface
from josephus.domain.person import Person

class LiteralUI(Interface):
    def __init__(self):
        super().__init__()
        self.use_reader: bool = False
        self.select_whether_use_reader()
        self.set_start()
        self.set_step()
        if self.use_reader:
            self.create_reader_()
        self.create_josephus_()
        self.show_participants()
        self.show_result()

    def set_start(self):
        try:
            start = input('please input start value: ')
            self.set_start_value(start)
        except ValueError:
            print('please input valid value of start')
            self.set_start()

    def set_step(self):
        try:
            step = input('please input step value: ')
            self.set_step_value(step)
        except ValueError:
            print('please input valid value of step')
            self.set_step()

    def create_reader_(self):
        filepath = input('please input the filepath: ')
        target_file = ''
        try:
            if '.zip' in filepath:
                target_file = input('please input the target filename: ')

            self.create_reader(filepath, target_file)
            self.use_reader = True
        except FileNotFoundError:
            print('Invalid filepath or target filename\nPlease invalid filepath')
            self.create_reader_()

    def create_josephus_(self):
        self.create_josephus()
        if not self.use_reader:
            self.add_person()

    def show_participants(self):
        print('information of participants')
        print(self.get_people_info(self.josephus.people))
        
    def show_result(self):
        print('result of josephus game')
        print(self.get_result())
    
    def select_whether_use_reader(self) -> None:
        print("Whether to load persons from file? No: 0\tYes: 1")
        opt = input()
        if opt == '0':
            self.use_reader = False
        else:
            self.use_reader = True
    
    def add_person(self):
        print("please input name and age of participant")
        go_on = 1
        while go_on:
            person = Person()
            person.name = input('please input name of participant: ')
            try:
                person.age = int(input('please input age of participant: '))
            except ValueError:
                print('invalid value of age, please input again')
                self.add_person()
                return 
            self.josephus.append(person)
            go_on = int(input("please select whether to continue to input\n1: YES\t0: NO\n"))
        