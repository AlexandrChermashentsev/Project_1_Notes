import Create_Note
import Generate_UUID
import os
import My_listdir
import Delete_Note
import Filter_Notes

flag = True
list_commands = ['1', '2', '3', '4', '5']
while flag:
    command = input("1 - Создать заметку\n\
2 - Посмотреть список заметок\n\
0 - Выход\n\
-> ")
    match command:
        case '1':
            command = input("В каком формате создать заметку?\n\
1 - json\n2 - csv\n-> ")
            body_note = input('Введите тело заметки: ')

            if command == '1' or command == 'json':
                Create_Note.Note(Generate_UUID.Create_uuid(), 'json', body_note)
            elif command == '2' or command == 'csv':
                Create_Note.Note(Generate_UUID.Create_uuid(), 'csv', body_note)
            else: print('Неверная команда! Возвращаемся в основное меню')

        case '2':
            command = input("Заметки какого формата вы хотели бы посмотреть?\n\
1 - json\n2 - csv\n-> ")
            
            if command == '1' or command == 'json':
                if os.path.isdir("Notes_json"):
                    os.chdir("Notes_json")
                    while flag:
                        My_listdir.lstdr('json')
                        command = input("1 - фильтрация заметок\n\
2 - редактировать заметку\n3 - удалить заметку\n0 - выйти в основное меню\n-> ")
                        
                        match command:
                            case '1':
                                pass
                            case '2':
                                pass
                            case '3':
                                name_file = input("Введите имя файла: ")
                                Delete_Note.Remove_Note(name_file)
                            case '0':
                                flag = False
                            case _:
                                print('Неверная команда!')
                    os.chdir("..")
                    flag = True

                else: print("Записок такого формата нет") 

            elif command == '2' or command == 'csv':
                if os.path.isdir("Notes_csv"):
                    os.chdir("Notes_csv")
                    My_listdir.lstdr('csv')
                    os.chdir("..")
                else: print("Записок такого формата нет") 
            else:
                print('Неверная команда! Возвращаемся в основное меню')

        case '0':
            flag = False
            
        case _:
            print("Error! Enter command")
