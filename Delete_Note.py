import os

def Remove_Note(name_file):
    # print(os.getcwd())
    if os.path.isfile(name_file):
        os.remove(name_file)
        print("Заметка удалена")
    else: print("Неверно введено имя файла")


