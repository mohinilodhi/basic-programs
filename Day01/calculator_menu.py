
print("🎉🎉welcome to this DAY01 small program🎉🎉")
print("today we make calculator")
#take value from user 

x= int(input("Enter the first number: ")) ##example 1,2,34,
y= int(input("Enter the second number: ")) ##example 1,2,34,


##TYPE1 (LONG METHOD)
addition = x+y  ##add
print(" the first value of",x,"the second value of" ,y,"addition of",x+y)

subtraction = x-y ##subtraction
print(" the first value of",x,"the second value of" ,y,"subtraction of",x-y)

multipliction = x*y ##product
print(" the first value of",x,"the second value of" ,y,"multiplication of",x*y)

division = x/y #divide
print(" the first value of",x,"the second value of" ,y,"division  of",x/y)

##TYPE2 (SHORT METHOD)
print("addition:", x+y)
print("subtraction:", x-y)
print("multiplication:", x+y)
print("division:", x+y)


if y !=0:
    print("division zero")
else:
    print("cannot divived by 0")
if x==y :
    print("this is equal")
else:
    print("its different")

print("thankyou for this ")



