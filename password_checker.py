import string


def get_password():
    while True:
        password = input("Enter your password: ")

        if len(password) < 8:
            print("\nPassword must contain at least 8 characters.")
            print("Please enter the password again.\n")
        else:
            return password


password = get_password()

print("Password Accepted!")