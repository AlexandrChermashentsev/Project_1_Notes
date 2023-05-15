from List_Formats import List_of_formats as LOF

def Repeat_Files_Format():
    return "1 - " + LOF()[0] + "\n2 - " + LOF()[1]

def Error_Command():
    print("Ошибка! Неверная команда")

def Empty_Notebook():
    print("Записок такого формата нет")

def Start_Menu():
    print("1 - Создать заметку\n\
2 - Посмотреть список заметок\n\
0 - Выход")

def Enter_Name_File():
    return "Введите имя файла (В формате: 'Id.формат'): "

def Format_Create_Note():
    print("В каком формате создать заметку?\n" + Repeat_Files_Format())

def List_Notes():
    return "Список заметок в формате "

def Lists_Menu():
    print("Заметки какого формата вы хотели бы посмотреть?\n" + Repeat_Files_Format())

def Menu_Filter_Edit_Del():
    print("1 - фильтрация заметок\n\
2 - редактировать заметку\n3 - удалить заметку\n0 - выйти в основное меню")

def Long_Separator():
    print("-------------------------------------------------------")