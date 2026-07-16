import string


def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score == 5:
        return "Very Strong"

    elif score == 4:
        return "Strong"

    elif score == 3:
        return "Medium"

    else:
        return "Weak"
    
def get_password():
    while True:
        password = input("Enter your password: ")

        if len(password) < 8:
            print("\nPassword must contain at least 8 characters.")
            print("Please enter the password again.\n")
        else:
            return password


password = get_password()

strength = check_strength(password)

print("Password Strength:", strength)

