from os import path, listdir
from time import strftime, strptime, ctime
from Sorted_time import date_and_time_sort as DaTS
import View
import Look_Notebook


def My_Filter_Notebook(command, filter_key):
    lst = []
    dctnry = {}
    for i in listdir():
        mtime = path.getmtime(i)
        time_str = strptime(ctime(mtime))
        t_stamp = strftime("%d-%m-%Y %H:%M:%S", time_str)

        if command in t_stamp.split('-')[filter_key]:
            dctnry[t_stamp] = i

    lst = list(dctnry.keys())
    lst = DaTS(lst)
    View.Long_Separator()
    for i in lst:
        print(str(dctnry[i]) + " - " + str(i))
    View.Long_Separator()
    
    print('Введите "1" - чтобы редактировать заметку\n\
или любой другой символ чтобы продолжить фильтровать или вернуться назад')
    command = input('-> ')
    if command == '1':
        print(View.Enter_Name_File())
        name_file = input('-> ')
        Look_Notebook.Edit_note(name_file)



def Find_Key_Filter_v2():
    flag = True
    list_commands = ['1', '2', '3']
    while flag:
        command = input("Фильтровать по:\n\
1 - числу дня\n2 - месяцу\n3 - году\n0 - назад\n-> ")
        
        if command in list_commands:
            filter_key = int(command) - 1
            filter = input('Введите фильтр: ')
            if command != '3' and len(filter) == 1:
                filter = '0' + filter     
            elif command == '3' and len(filter) == 2:
                filter = '20' + filter

            My_Filter_Notebook(filter, filter_key)
        elif command == '0':
            flag = False
        else: View.Error_Command()            
