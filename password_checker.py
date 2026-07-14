import string
import random


SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(c in SPECIAL for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback


def suggest_password(base_password):
    chars = list(base_password)

    chars.append(random.choice(string.ascii_uppercase))
    chars.append(random.choice(string.ascii_lowercase))
    chars.append(random.choice(string.digits))
    chars.append(random.choice(SPECIAL))

    random.shuffle(chars)

    while len(chars) < 12:
        chars.append(
            random.choice(
                string.ascii_letters + string.digits + SPECIAL
            )
        )

    random.shuffle(chars)

    return "".join(chars)


def main():
    password = input("Enter your password: ")

    strength, feedback = password_strength(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)

    print("\nSuggested Strong Password:")
    print(suggest_password(password))


if __name__ == "__main__":
    main()