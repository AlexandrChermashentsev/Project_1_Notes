from os import path, remove

def Remove_Note(name_file):
    if path.isfile(name_file):
        remove(name_file)
        print("Заметка удалена")
    else: print("Неверно введено имя файла")


