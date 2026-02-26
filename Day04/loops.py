##day 04 here you are welcome to this program
##loops are helpful in repewating something 
print("welcome to the concept of loops ")

#example of for
for i in range(5):
    print("hello")

for a in range(12):
    print("mohini lodhi")

for i in range(2, 8):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

for i in range(1, 15):
    if i % 2 == 0:
        print(i,"thi is even")
    else:
        print(i,"this is odd")


##ATM MACHINE REAL LIFE EXAMPLE FOR TIS PROGRAM AND I ONLY WANT TO KNOW ABOUT THIS

print("In this program i want to use loop or condition check  ")

user_money = int(input("Enter amount which you want to withdraw: "))

money = 5000

if user_money < money:
    print("congrats! you can withdraw money ")
else:
    print("sorry their is not enough money available ")