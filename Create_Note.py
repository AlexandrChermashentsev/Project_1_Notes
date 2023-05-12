# import time
# import uuid
# import Generate_UUID
import os


class Note():
    def __init__(self, uuid, format_file, body):
        if not os.path.isdir("Notes_" + format_file):
            os.mkdir("Notes_" + format_file)

        os.chdir("Notes_" + format_file)

        with open(uuid + '.' + format_file, 'a') as data:
            data.write(body)
        print("Заметка создана!")
        os.chdir("..")

