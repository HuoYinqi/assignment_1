import zipfile

from josephus.use_cases.josephus import Josephus
from josephus.reader.csv_reader import CSVReader
from josephus.reader.txt_reader import TxtReader
from josephus.domain.person import Person


def creat_josephus(reader=None):
    print("Creat josephus ring")
    jos = Josephus(reader)
    if len(jos.people) == 0:
        print("please input name and age of participant")
        go_on = 1
        while go_on:
            person = Person()
            person.name = input("please input name:")
            person.age = int(input("please input age:"))
            jos.append(person)
            go_on = int(input("please select whether to continue to input\n1: YES\t0: NO\n"))

    total = len(jos.people)
    
    while True:
        try:
            jos.start = int(input("please input the value of start position:"))
            if jos.start > total or jos.start < 1:
                print(f"please input integer from 1 to {total}!")
                continue
            break
        except ValueError:
            print(f"please input integer from 1 to {total}!")

    while True:        
        try:
            jos.step = int(input("please input the value of josephus step:"))
            if jos.step < 1:
                print("please input positive integer!")
                continue
            break
        except ValueError:
            print(f"please input integer from 1 to {total}!")
    return jos

def creat_reader():
    print("creat persons of josephus\nplease select one method below to create persons")
    n = int(input("1: from .txt 2: from .csv 3:from .zip 4: input from screen\n"))
    if n == 1:
        reader = persons_from_txt()
    elif n == 2:
        reader = persons_from_csv()
    elif n == 3:
        reader = persons_from_zip()
    else:
        reader = None

    return reader


def persons_from_txt():
    while True:
        try:
            file_path = input("please input txt file path:")
            txt_reader = TxtReader(file_path)
            break
        except FileNotFoundError:
            print("invalid file path, please input valid path!")
    return txt_reader

def persons_from_csv():
    while True:
        try:
            file_path = input("please input csv file path:")
            csv_reader = CSVReader(file_path)
            break
        except FileNotFoundError:
            print("invalid file path, please input valid path!")
    return csv_reader 

def persons_from_zip():
    while True:
        file_path = input("please input zip file path:")
        if zipfile.is_zipfile(file_path):
            break
        print("invalid file path, please input valid path!")

    while True:
        target_file = input("please target file in zip:")
        try:
            if '.txt' in target_file:
                zip_reader = TxtReader.from_zip(file_path, target_file)
            elif '.csv' in target_file:
                zip_reader = CSVReader.from_zip(file_path, target_file)
            else:
                print("please input valid file name!")
                continue
            break
        except KeyError:
            print("No such file in zip, please input file name again:")
    
    return zip_reader

def print_result(jos):
    print("-----result-----")
    size = len(jos.people)
    index = 1
    for each in jos:
        if index == size:
            print(f"winner: {each.name}\t{each.age}")
        else:
            print(f"elimination: {each.name}\t{each.age}") 
        index += 1
    


if __name__ == '__main__':
    reader = creat_reader()
    jos = creat_josephus(reader)
    print_result(jos)



# p = Person(input())
# print(type(p))
# print(f"name:{p.name}, age:{p.age}")

# jos = Josephus(reader)

# jos.start = int(input("input the value of start:"))
# jos.step = int(input("input the value of step:"))

# for each in jos:
#     print(f"elimination: {each.name}\t{each.age}")
