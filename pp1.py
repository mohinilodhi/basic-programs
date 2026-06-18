# day 19 

print("===   🎓🎯 STUDENT RECORD SYSTEM🎯   ===")

students = ["Mohini",
            "akash",
            "abhay"]

while True:
    print("1. Add Student ")
    print("2. View Students ")
    print("3. Search Student ")
    print("4. Delete Student")
    print("5. Total Students ")
    print("6. Exit ")
   
    user = int(input("enter your choice: "))

    if user == 1:
        name = input("enter your name: ")
        students.append(name)
        print(students)

    elif user == 2:
        for student in students:
            print(student)

    elif user == 3:
        search_name = input("enter name: ")
        

        for student in students:
         if search_name.lower() in student.lower():
            found = True
            print("Student Found")
         

    elif user == 4:
        delete_name = input("enter your name: ")
        

        for student in students:
         
         if delete_name.lower() in student.lower():


            students.remove(student)
            

            print("Student Deleted Successfully")
            break
    elif user == 5:
       length = len(students)
       print(length)
    
    elif user == 6:
       print("👋 Exiting Program...")
       break



           
#DAY 20
print("📂 FILE READER & WRITER")



while True:

    print("1. Write Note")
    print("2. Read Note")
    print("3. Exit")

    user = int(input("Enter choice: "))

    if user == 1:
       note = input("enter note: ")
       file = open("notes.txt","w")
       file.write(note)
       file.close()
       
    
    elif user == 2:
       file = open("notes.txt", "r")
       data = file.read()
       print(data)
       file.close()
    
    elif user == 3:
       print("👋 Exiting Program...")
       break

#day 21
print("🔥 DAY 21 — MCQ TEST SYSTEM PROJECT")


score = 0
print("Q1. Python kisne banayi?")


print("A. James Gosling")
print("B. Guido van Rossum")
print("C. Dennis Ritchie")
print("D. Elon Musk")

correct_answer = "B"

user = input("Enter answer: ").upper()

if user == "B":
   print("correct answer")
   score =+ 1

else:
   print("false")



print("Q2. List me item add karne ke liye kaunsa method use hota hai?")

print("A. remove")
print("B. len")
print("C append")
print("D. read")

correct_answer = "C"

user = input("Enter answer: ").upper()

if user == correct_answer:
   print("correct answer")
   score =+ 1

else:
   print("false")
print("\nQ3. List ki length nikalne ke liye?")
print("A. write()")
print("B. len()")
print("C. read()")
print("D. append()")

user = input("Enter Answer: ").upper()

if user == "B":
    print(" Correct")
    score += 1
else:
    print(" Wrong")

# Q4
print("\nQ4. User se input lene ke liye?")
print("A. input()")
print("B. print()")
print("C. read()")
print("D. write()")

user = input("Enter Answer: ").upper()

if user == "A":
    print(" Correct")
    score += 1
else:
    print(" Wrong")

# Q5
print("\nQ5. Loop ko stop karne ke liye?")
print("A. continue")
print("B. remove")
print("C. break")
print("D. append")

user = input("Enter Answer: ").upper()

if user == "C":
    print(" Correct")
    score += 1

else:
    print(" Wrong")

# Final Result
print(" RESULT ")
print("Final Score =", score, "/ 5")

if score == 5:
    print(" Excellent!")
elif score >= 3:
    print(" Good Job!")
else:
    print(" Keep Practicing!")


#day 22
# DAY 22 - ROCK PAPER SCISSORS

# DAY 22 - ROCK PAPER SCISSORS

import random

print("🔥 Rock Paper Scissors Game 🔥")

while True:

    print("\n1 = Rock")
    print("2 = Paper")
    print("3 = Scissors")
    print("4 = Exit")

    user = int(input("Enter your choice: "))

    if user == 4:
        print("👋 Exiting Game...")
        break

    if user < 1 or user > 4:
        print("❌ Invalid Choice")
        continue

    computer = random.randint(1, 3)

    # Show computer choice
    if computer == 1:
        print("💻 Computer Chose: Rock")
    elif computer == 2:
        print("💻 Computer Chose: Paper")
    else:
        print("💻 Computer Chose: Scissors")

    # Game Logic
    if user == computer:
        print("🤝 It's a Draw")

    elif user == 1 and computer == 3:
        print("🎉 You Win!")

    elif user == 2 and computer == 1:
        print("🎉 You Win!")

    elif user == 3 and computer == 2:
        print("🎉 You Win!")

    else:
        print("💻 Computer Wins!")