from os import path, mkdir, chdir
from List_Formats import Return_Length_Headline as RLH

class Note():

    def __init__(self, uuid, format_file):
        if not path.isdir("Notes_" + format_file):
            mkdir("Notes_" + format_file)

        chdir("Notes_" + format_file)
        headline = input('Введите заголовок заметки: ')
        flag = True
        while flag:
            if len(headline) >= RLH() or ";" in headline:
                headline = input('Введите заголовок заметки не более ' + str(RLH())
                                + ' символов: ')
            else: 
                flag = False

        body_note = input('Введите тело заметки: ')
        with open(uuid + '.' + format_file, 'a') as data:
            data.write(headline + "\n")
            data.write(body_note)
        print("Заметка создана!")
        chdir("..")
