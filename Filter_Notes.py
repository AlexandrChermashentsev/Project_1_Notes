import os
import time

# Учесть верхний и нижний регистр. Попытаться сломать этот блог

def My_Filter_Notebook(mkey, filter_key):
    # mdict = {}
    # mlist = []
    # mtuple = ()
    # keys_list = ['DayOfWeek', 'Month', 'Day', 'Time', 'Year']
    for i in os.listdir():
        mtime = os.path.getmtime(i)
        if mkey in time.ctime(mtime).split()[filter_key]:
            print(i + ' - ' + time.ctime(mtime))
        # mlist.append(time.ctime(mtime).split())

def Find_key_filter(format_notes):
    os.chdir("Notes_" + format_notes)
    list_commands = ['1', '2', '3', '4', '5']
    flag = True
    for i in os.listdir():
        mtime = os.path.getmtime(i)
        print(i + ' - ' + time.ctime(mtime))

    while flag:
        command = input("Фильтровать по:\n\
1 - дню недели\n2 - месяцу\n3 - числу месяца\n4 - времени редактирования/создания\n\
5 - году редактирования/создания\n0 - назад\n-> ")
        if command in list_commands:
            filter_key = int(command) - 1
            command = input('Введите фильтр: ')
            My_Filter_Notebook(command, filter_key)
        elif command == '0':
            flag = False
        else: print("Неверная команда")

Find_key_filter('csv')