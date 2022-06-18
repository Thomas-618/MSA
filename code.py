def start_menu():
    print(  "\nSelect option from Menu",
            "-----------------------",
            "1. Login",
            "2. Create User account", sep="\n")

    while True:
        print()
        option = input("\nWould you like to login or create account? ")
        if option != "1" and option != "2":
            print("\nERROR: Enter a 1 or 2")
            continue
        else:
            return option


def login_user(user_name, user_pass):
    while True:    
        file = open("users.txt", "r")
        user_found = False
        for line in file:
            credentials = line.split(",")
            if credentials[0] == user_name and credentials[1].rstrip() == user_pass:
                user_found = True
                break
        if user_found:
            print("User Logged in!")
            return True
        else:
            print(f"User: {user_name} with password, {user_pass} not found.\n")
            return False


def create_user(user_name, user_pass):
    while True:
        user_length = len(user_name)
        pass_length = len(user_pass)

        if (user_length >= 4 and user_length <= 16) and (pass_length >= 6 and pass_length <= 12):
            file = open("users.txt", "a")
            file.write(f"{user_name}, {user_pass}\n")
            file.close()
            print("User Created")
            return True
        else:
            print("ERROR: Invalid username or password length")
            return False


def main():
    option = start_menu()
    while True:
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")
        match option:
            case "1":
                if login_user(user_name, user_pass):
                    break
            case "2":
                if create_user(user_name, user_pass):
                    break
main()