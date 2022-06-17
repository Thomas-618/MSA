import math
 
#defines hashmap used to convert number grades to their corresponding leters
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
    #prompts user for starting function
    user_decision = input("Welcome to student checker! \n 1. Sign in to an existing account \n 2. Create a new account\n")
    if user_decision == "1":
        accounts = open("database.txt", "r").readlines()
        username = input("Username: ")
        password = input("password: ")
        #iterates through the accounts' database text file to check if the user-provided info matches an existing account
        for line in accounts:
            values = line.split(", ")
            if values[0] == username and values[1] == password:
                print("Account Signed into!")
                loop = False
                break
            else:
                print("Invalid Username or Password")
    elif user_decision == "2":
        username = input("Username: ")
        password = input("password: ")
        #checks if user-provided account info is suitable based on length credentials
        if not 4 < len(username) < 16  or not 6 < len(password) < 12:
            print("Username must be be between 4 and 16 characters, Password must be between 6 and 12 characters")
        else:
            #creates a new account in the atabase text file using the user-provided info
            file = open("database.txt", "a")
            file.write(f"\n{username}, {password}")
            print("New Account Created!")
            loop = False
            break
#prompts user for info on student grades and creates hashmap in order to store them
grades = {}
amount_of_student_grades = int(input("How many student grades would you like to enter? "))
#iterates though the user-provided number of students, taking each student's name and number grade
while True:    
    for i in range(amount_of_student_grades):
        student_name = input("What is the student's name? ")
        grades[student_name] = float(input("What is the student's grade? "))
    #ensures that the user provided grade is suitable for the calculation (being between 0 and 100)
    try:
        for grade in grades:
            print(f"{grade}: {grades[grade]}: {grade_conversion[round(grades[grade] / 10) * 10]}")
    except KeyError or ValueError:
        print("All grades must be between 0 and 100")
        grades = {}
    else:
        break
#calculates and prints average user grades using the user-provided information
print(f"Average grade: {sum(grades.values()) / amount_of_student_grades}")
