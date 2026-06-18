import time

seconds = int(input("Enter seconds: "))
time.sleep(3)
print(" i am good")

import time

print(3)
time.sleep(1)

print(2)
time.sleep(1)

print(1)
time.sleep(1)

print("Time's Up!")

import time

number = 10

while number > 0:
    print(number)
    time.sleep(1)
    number -= 1

print("Time's Up!")


number = 10

while number > 0:
    print(number)
    time.sleep(1)
    number -= 1

print("Time's Up!")



import time

user = int(input())

while user > 0:
    print(user)
    time.sleep(2)
    user -= 1
    print("times up")

#DAY 24

while True:
   print("1. Addition")
   print("2. Subtraction ")
   print("3. Multiplication")
   print("4. Division")
   print("5. Exit")

   user = int(input("option1/2/3/4/5: "))
   a = int(input("enter first: "))
   
   b = int(input("enter first: "))

   if user == 1:
       print(a+b)
   elif user == 2:
       print(a-b)
   elif user == 2:
       print(a*b)
   elif user == 2:
       print(a/b)
   elif user == 5:
       print("exit")
       break
       

       