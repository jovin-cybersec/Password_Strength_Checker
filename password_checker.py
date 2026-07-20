import string
import random


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
    

def generate_suggestions(password):

    suggestions = []

    # Suggestion 1
    suggestions.append(password.swapcase())

    # Suggestion 2
    suggestions.append(password[::-1])

    # Suggestion 3
    chars = list(password)
    random.shuffle(chars)
    suggestions.append("".join(chars))

    return suggestions

def get_password():
    while True:
        password = input("Enter your password: ")

        if len(password) < 8:
            print("❌ Password must be at least 8 characters long.\n")
            print("Please enter the password again.\n")
        else:
            return password


password = get_password()

strength = check_strength(password)

print("Password Strength:", strength)

print("\nSuggested Passwords:")

for p in generate_suggestions(password):
    print(p)

