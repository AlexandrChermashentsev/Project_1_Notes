from os import chdir, listdir

def Fool_Proof(command):
    flag = True
    while flag:
        for i in listdir():
            if command == i:
                flag = False
                return command
        else: command = input("Такого файла нет. Введите имя файла: ")

def Edit_note(name_file):
    # chdir("Notes_" + 'json') # Убрать
    flag = True
    data = open(name_file, 'r+')
    print("---------------------------------------")
    for line in data:
        print(line, end='')
    data.close()
    print()
    print("---------------------------------------")
    while flag:
        command = input("Что вы хотите изменить?\n1 - заголовок заметки(не более 10 символов)\n2 - текст заметки\n0 - назад\n-> ")

        match command:
            case '1':
                command = input("Введите новый текст заголовка: ")
                if len(command) > 10 or ";" in command:
                    print('Ошибка')
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
                    lines[1] = command
                with open(name_file, 'w') as f:
                    for i in lines:
                        f.write(i)

            case '0':
                flag = False
            case _:
                print('Неверная команда!')
    # data.close()


# Edit_note('3a646186-a0f8.json') # Убрать