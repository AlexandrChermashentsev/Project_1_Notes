from Generate_UUID import Create_uuid as CU
from List_Formats import List_of_formats as LOF
from os import path, chdir
import Obj_Note
import My_listdir
import Delete_Note
import Filter_Notes
import Look_Notebook
import View

def Program():
    flag = True
    while flag:
        View.Start_Menu()
        command = input("-> ")
        match command:

            case '1': # Создание заметки
                View.Format_Create_Note()
                command = input("-> ")
                if command == '1' or command == LOF()[0]: # json
                    Obj_Note.Note(CU(), LOF()[0])
                elif command == '2' or command == LOF()[1]: # csv
                    Obj_Note.Note(CU(), LOF()[1])
                else: View.Error_Command()

            case '2': # Работа со списком заметок
                while flag:
                    View.Lists_Menu()
                    command = input("-> ")
                
                    if command == '1' or command == LOF()[0]: # json
                        format_notes = LOF()[0]
                        flag = False
                    elif command == '2' or command == LOF()[1]: # csv
                        format_notes = LOF()[1]
                        flag = False
                    else: View.Error_Command()
                flag = True
                
                if path.isdir("Notes_" + format_notes):
                    print(View.List_Notes() + format_notes)
                    chdir("Notes_" + format_notes)

                    while flag:
                        My_listdir.lstdr()
                        View.Menu_Filter_Edit_Del()
                        command = input("-> ")                        
                        match command:
                            case '1': # Фильтрация
                                Filter_Notes.Find_Key_Filter_v2()
                            case '2': # Редактирование
                                print(View.Enter_Name_File())
                                name_file = input()
                                Look_Notebook.Edit_note(name_file)
                            case '3': # Удаление
                                print(View.Enter_Name_File())
                                name_file = input()
                                Delete_Note.Remove_Note(name_file)
                            case '0': # Назад
                                flag = False
                            case _: # Ошибка ввода
                                View.Error_Command()

                    chdir("..")
                    flag = True
                else: View.Empty_Notebook() 

            case '0': # Выход из программы
                flag = False
                
            case _: # Ошибка ввода
                View.Error_Command()
