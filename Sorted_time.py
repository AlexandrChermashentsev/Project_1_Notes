import datetime

def date_sort(timestamps):
    dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps]
    dates.sort()
    # print(dates)
    sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
    # for i in sorteddates:
        # print(i)

def date_and_time_sort(timestamps):
    dates = [datetime.datetime.strptime(ts, "%d-%m-%Y %H:%M:%S") for ts in timestamps]
    dates.sort()
    # print(dates)
    sorteddates = [datetime.datetime.strftime(ts, "%d-%m-%Y %H:%M:%S") for ts in dates]
    # for i in sorteddates:
        # print(i)
    return sorteddates

timestamps = ['2011-06-2', '2011-08-05', '2011-02-04', '2010-1-14', 
              '2010-12-13', '2010-1-12', '2010-2-11', '2010-2-07', 
              '2010-12-02', '2011-11-30', '2010-11-26', 
              '2010-11-23', '2010-11-22', '2010-11-16']

timestamps_2 = ['12-05-2026 14:29:41', '12-05-2023 14:23:36', '14-06-2023 15:23:36', '22-05-2023 14:23:36', 
                '12-05-2023 14:22:36']

# date_sort_2(timestamps_2)
# ['2010-01-12', '2010-01-14', '2010-02-07', '2010-02-11', '2010-11-16', '2010-11-
# 22', '2010-11-23', '2010-11-26', '2010-12-02', '2010-12-13', '2011-02-04', '2011
# -06-02', '2011-08-05', '2011-11-30']