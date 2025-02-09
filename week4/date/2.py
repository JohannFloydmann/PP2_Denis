import datetime
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

for day in (today, yesterday, tomorrow):
    print(day.strftime("%x"))