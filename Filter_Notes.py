import os
import time
import Sorted_time

# Учесть верхний и нижний регистр. Попытаться сломать этот блог

def My_Filter_Notebook(command, filter_key):
    list1 = []
    d = {}
    # My_listdir.lstdr()
    for i in os.listdir():
        mtime = os.path.getmtime(i)
        time_str = time.strptime(time.ctime(mtime))
        t_stamp = time.strftime("%d-%m-%Y %H:%M:%S", time_str)

        # print("t_stamp = " + t_stamp.split()[filter_key])
        if command in t_stamp.split('-')[filter_key]:
            time_str = time.strptime(time.ctime(mtime))
            t_stamp = time.strftime("%d-%m-%Y %H:%M:%S", time_str)
            d[t_stamp] = i

    list1 = list(d.keys())
    list1 = Sorted_time.date_and_time_sort(list1)
    for i in list1:
        print(str(d[i]) + " - " + str(i))

def Find_Key_Filter_v2():
    # os.chdir("Notes_" + 'json')
    # My_listdir.lstdr()
    flag = True
    list_commands = ['1', '2', '3']
    while flag:
        command = input("Фильтровать по:\n\
1 - числу дня\n2 - месяцу\n3 - году\n0 - назад\n-> ")
        if command in list_commands:
            filter_key = int(command) - 1
            command = input('Введите фильтр: ')
            My_Filter_Notebook(command, filter_key)
        elif command == '0':
            flag = False
        else: print("Неверная команда")            

# Find_Key_Filter_v2()