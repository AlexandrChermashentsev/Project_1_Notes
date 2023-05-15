from os import path, listdir
from time import strftime, strptime, ctime
from Sorted_time import date_and_time_sort as DaTS
from List_Formats import Return_Length_Headline as RLH
from View import Long_Separator

def lstdr():
    list1 = []
    d = {}
    for i in listdir():
        mtime = path.getmtime(i)
        with open(i) as file:
            headline = file.readline()[:-1]

        time_str = strptime(ctime(mtime))
        t_stamp = strftime("%d-%m-%Y %H:%M:%S", time_str)

        d[t_stamp] = i + " ; " + headline + " " * (RLH() - len(headline))
    list1 = list(d.keys())
    list1 = DaTS(list1)
    Long_Separator()
    for i in list1:
        print(str(d[i]) + " ; " + str(i))
    Long_Separator()
