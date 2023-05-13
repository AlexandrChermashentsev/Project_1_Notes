# import time
# import uuid
# import Generate_UUID
import os


class Note():

    def __init__(self, uuid, format_file):
        if not os.path.isdir("Notes_" + format_file):
            os.mkdir("Notes_" + format_file)

        os.chdir("Notes_" + format_file)
        headline = input('Введите заголовок заметки: ')
        flag = True
        while flag:
            if len(headline) > 10 or ";" in headline:
                headline = input('Введите заголовок заметки не более 10 символов: ')
            else: 
                flag = False

        body_note = input('Введите тело заметки: ')
        with open(uuid + '.' + format_file, 'a') as data:
            data.write(headline + "\n")
            data.write(body_note)
        print("Заметка создана!")
        os.chdir("..")

