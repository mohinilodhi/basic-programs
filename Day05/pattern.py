##Day 05
### create star pattern programs 

num = int(input("Enter the number of rows: "))

for i in range(1, num + 1):     ##outer loops row
    for j in range (i):         ##inner loops (stars)
        print("*", end="")      ##same line me star
    print()                     ##next line


##for reverse

num = int(input("Enter the number of rows: "))

for i in range(num ,0, -1):
    for j in range(i):
        print("*", end="")
    print()

###exam result check 
m1 = float(input("Enter amit`s maths marks: "))
m2 = float(input("Enter amit`s physics marks: "))
m3 = float(input("Enter amit`s chemistry marks: "))
m4 = float(input("Enter amit`s IP marks: "))
m5 = float(input("Enter amit`s english marks: "))

addition = m1+m2+m3+m4+m5
avg = addition/5

##condition check
if avg>= 75:
    print("distinction")
elif avg >= 60:
    print("first division")
elif avg >= 40:
    print("pass")
else:
    print("fail")
    