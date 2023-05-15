from os import listdir, path
from List_Formats import Return_Length_Headline as RLH
import View

def Edit_note(name_file):
    if path.isfile(name_file):
        flag = True
        count = 1
        while flag:
            data = open(name_file, 'r')
            View.Long_Separator()
            for line in data:
                match count:
                    case 1:
                        print('\033[3;0;0m', line, end='')
                        count+= 1
                    case _:
                        print(line, end='')
            data.close()
            print()
            View.Long_Separator()
            command = input("Что вы хотите изменить?\n1 - заголовок заметки(не более " + str(RLH()) 
                            + " символов) (первая строка)\n2 - текст заметки (вторая строка)\n0 - назад\n-> ")

            match command:
                case '1':
                    command = input("Введите новый текст заголовка: ")
                    if (len(command) >= RLH() or ";" in command) and len(command) == 0:
                        print(View.Error_Command())
                    else:
                        with open(name_file, 'r') as f:
                            lines = f.readlines()
                        lines[0] = command + '\n'
                        with open(name_file, 'w') as f:
                            for i in lines:
                                f.write(i)
                                                        
                case '2':
                    command = input("Введите новый текст заметки: ")
                    with open(name_file, 'r') as f:
                        lines = f.readlines()

                    if len(lines) == 1:
                        lines.append(command)
                    else: lines[1] = command

                    with open(name_file, 'w') as f:
                        for i in lines:
                            f.write(i)

                case '0':
                    flag = False
                case _:
                    View.Error_Command()
    else: print("Неверно введено имя файла")
