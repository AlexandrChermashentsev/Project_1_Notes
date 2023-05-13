import os
import time
import datetime
import Sorted_time

def lstdr():
    # print("Список заметок в формате " + format_file)
    list1 = []
    d = {}
    x = 10
    # headline_list = []
    # os.chdir("Notes_" + 'json') # Убрать
    for i in os.listdir():
        mtime = os.path.getmtime(i)
        # m_ti = time.ctime(mtime)
        with open(i) as file:
            headline = file.readline()[:-1]

        time_str = time.strptime(time.ctime(mtime))
        t_stamp = time.strftime("%d-%m-%Y %H:%M:%S", time_str)
        # print(i + " - " + t_stamp)
        d[t_stamp] = i + " ; " + headline + " " * (x - len(headline))
    list1 = list(d.keys())
    list1 = Sorted_time.date_and_time_sort(list1)
    for i in list1:
        print(str(d[i]) + " ; " + str(i))

    # os.chdir("..") # Убрать

# lstdr()


# my_dict = {1: "a", 2: "b"} 
# print("The length of the dictionary is {}".format(len(my_dict)))