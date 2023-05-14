from os import path, listdir
from time import strftime, strptime, ctime
from Sorted_time import date_and_time_sort as DaTS
import View


def My_Filter_Notebook(command, filter_key):
    lst = []
    dctnry = {}
    for i in listdir():
        mtime = path.getmtime(i)
        time_str = strptime(ctime(mtime))
        t_stamp = strftime("%d-%m-%Y %H:%M:%S", time_str)

        if command in t_stamp.split('-')[filter_key]:
            time_str = strptime(ctime(mtime))
            t_stamp = strftime("%d-%m-%Y %H:%M:%S", time_str)
            dctnry[t_stamp] = i

    lst = list(dctnry.keys())
    lst = DaTS(lst)
    for i in lst:
        print(str(dctnry[i]) + " - " + str(i))

def Find_Key_Filter_v2():
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
        else: View.Error_Command()            
