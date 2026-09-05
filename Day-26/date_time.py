from datetime import timedelta
from datetime import date
from datetime import datetime
from datetime import time

today = date.today() 
print(today)
print(today.day) 
print(today.month) 
print(today.year)
print(today.weekday())  


year,month,dt=list(map(int,input("YYYY-MM-DD : ").split("-")))
print(date(year,month,dt),type(date(year,month,dt)))

res=time(23,59,59)
print(res)

n=datetime.now()
print(n)
print(n.day) 
print(n.month) 
print(n.year)
print(n.weekday()) 
print(n.strftime('%D-%m-%Y %H:%M:%S'))
print(n.strftime('%D-%m-%Y %H:%M:%S %p'))
print(n.strftime('%d %b %Y %H:%M:%S %p'))
print(n.strftime('%d %B %Y %H:%M:%S %p'))
print(n.strftime('%a %d %Y %H:%M:%S %p'))
print(n.strftime('%A %d %Y %H:%M:%S %p'))

t = date.today()
n = datetime.now()
t7 = t + timedelta(days=7)
t5 = t - timedelta(days=5)
n15 = n + timedelta(minutes=15)

print(t, t7)
print(t, t5)
print(n, n15)
