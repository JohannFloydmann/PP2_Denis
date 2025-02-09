import datetime

def drop(day : datetime.datetime):
    return day.replace(microsecond=0)

x = datetime.datetime.now()
print(x)
print(drop(x))