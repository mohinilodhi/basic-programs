## import time and datetime
import datetime

d1 = datetime.date(2026, 2, 21)
d2 = datetime.date(2026, 3, 16)

difference = d2 - d1

print(difference.days)


now = datetime.datetime.now()
print(now)

today = datetime.date.today()
print(today)

dob_input= input("enter your dob(DD-MM-YY): ")

# string ko date me convert kar dega 
dob = datetime.datetime.strptime(dob_input, "%d-%m-%Y").date()

today = datetime.date.today()
age = today - dob
print("total days lived:" , age.days)
print(age.days)

current__time = datetime.datetime.now().time()
print (current__time)

import time
print(time.time())

print("start")
time.sleep(2)
print("end")

print(time.localtime())

##calender 
#for whole year 
import calendar
print(calendar.calendar(2026))
#for a month
print(calendar.calendar(2026,3))
