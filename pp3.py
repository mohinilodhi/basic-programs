
#DAY 24
print("      CALCULATOR    ")
while True:
   print("1. Addition")
   print("2. Subtraction ")
   print("3. Multiplication")
   print("4. Division")
   print("5. Exit")

   user = int(input("ENTER CHOICE: "))
    
    
   a = int(input("enter first: "))
   b = int(input("enter SEC: "))

   if user == 1:
       print(a+b)
   elif user == 2:
       print(a-b)
   elif user == 3:
       print(a*b)
   elif user == 4:
       print(a/b)
   elif user == 5:
       print("exit")
       break
       
