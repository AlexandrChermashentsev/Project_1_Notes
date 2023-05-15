import datetime

def date_sort(timestamps):
    dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps]
    dates.sort()
    sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]

def date_and_time_sort(timestamps):
    dates = [datetime.datetime.strptime(ts, "%d-%m-%Y %H:%M:%S") for ts in timestamps]
    dates.sort()
    sorteddates = [datetime.datetime.strftime(ts, "%d-%m-%Y %H:%M:%S") for ts in dates]
    return sorteddates

