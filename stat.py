import os.path
import statistics


def get_file_name():
    while True:
        #prompt user to enter file name
        user_input = input("Please enter a file name: ")
        #make sure user entered a value. Re prompt if not
        if user_input == "":
            print("ERROR: please enter a value.\n")
            continue
        elif not os.path.exists(user_input):
            print("ERROR: File does not exist.\n")
            continue
        else:
            break
    #else return the value
    return user_input


#Function to load numbers from file into list
#Parameters: file name
#returns a list of numbers
def load_numbers_list(file_name):
    numbers_list = []
    #open the file
    file = open(file_name, "r")
    #read file line by line
    for number in file:
        #convert to int and append numbers to a list
        numbers_list.append(int(number))
    #return the list
    return numbers_list


def calculate_stats(file, nums):
    return {
        "File Name": file,
        "Sum": sum(nums),
        "Count": len(nums),
        "Average": statistics.mean(nums),
        "Maximum": max(nums),
        "Minimum": min(nums),
        "Range": max(nums) - min(nums),
        "Median": statistics.median(nums),
        "Mode": statistics.mode(nums),
    }


def display_info(stats):
    print("\n")
    for key, value in zip(stats.keys(), stats.values()):
        print(f"{key}: {value}")
    print("\n")


def main():
    #ask user to enter filename and open that file
    file_name = get_file_name()
    
    #load number from file into a list
    list_of_numbers = load_numbers_list(file_name)

    #check the length of the list
    if len(list_of_numbers) == 0:
        print("File was empty")
    elif len(list_of_numbers) == 1:
        print("Only one number in file")
    else:
        stats = calculate_stats(file_name, list_of_numbers)
        display_info(stats)

main()