import math
 
grade_conversion = {
    100: "A",
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    50: "F",
    40: "F",
    30: "F",
    20: "F",
    10: "F",
    0: "F",
}
 
 
loop = True
while loop:
    user_decision = input("Welcome to student checker! \n 1. Sign in to an existing account \n 2. Create a new account\n")
    if user_decision == "1":
        accounts = open("database.txt", "r").readlines()
        username = input("Username: ")
        password = input("password: ")
        for line in accounts:
            values = line.split(", ")
            if values[0] == username and values[1] == password:
                loop = False
                break
    elif user_decision == "2":
        username = input("Username: ")
        password = input("password: ")
        if not 4 < len(username) < 16  or not 6 < len(password) < 12:
            print("Username must be be between 4 and 16 characters, Password must be between 6 and 12 characters")
        else:
            file = open("database.txt", "a")
            file.write(f"\n{username}, {password}")
            loop = False
            break
 
grades = {}
amount_of_student_grades = int(input("How much student grades would you like to enter? "))
for i in range(amount_of_student_grades):
    student_name = input("What is the student's name? ")
    grades[student_name] = float(input("What is the student's grade? "))
for grade in grades:
    print(f"{grade}: {grades[grade]}: {grade_conversion[round(grades[grade] / 10) * 10]}")
print(f"Average grade: {sum(grades.values()) / amount_of_student_grades}")