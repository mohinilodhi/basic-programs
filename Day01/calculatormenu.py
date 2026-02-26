print("🧮welcome to this advance level calculator")


num1= float(input("Enter your number: "))
num2= float(input("Enter your number: "))

print("choose operation")

print("1.add")
print("2.sub")
print("3.product")
print("4.divide")


choice = input("enter your choice(1/2/3/4): ")

if choice == '1':
    print("result:",num1+num2 )

elif choice == '2':
    print("result:",num1-num2 )

elif choice == '3':
    print("result:",num1*num2 )

elif choice == '4':
    if num2 !=0:
      print("result:",num1/num2 )
    else:
        print("cannot divide by zero")

else:
    print("invalid choice")

