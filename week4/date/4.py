import datetime
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)

print((today - yesterday).total_seconds())