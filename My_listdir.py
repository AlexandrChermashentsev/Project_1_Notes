import os
import time

def lstdr(format_file):
    print("Список заметок в формате " + format_file)
    # os.chdir("Notes_" + format_file)
    for i in os.listdir():
        mtime = os.path.getmtime(i)
        print(i + ' - ' + time.ctime(mtime))
    # os.chdir("..")
