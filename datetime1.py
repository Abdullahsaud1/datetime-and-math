import datetime
date =datetime.date(2023 , 5 , 26)
time = datetime.time (13 , 33 , 59)
new = datetime.datetime.today()
print(date)
print(date.strftime('%A %B %Y'))
print(time)
print(time.strftime('%I %M %S'))
print(new)
