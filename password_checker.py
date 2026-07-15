import random
import string
import re


def check_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
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


def alternate_case(text):
    result = ""

    for i, ch in enumerate(text):
        if ch.isalpha():
            if i % 2 == 0:
                result += ch.lower()
            else:
                result += ch.upper()
        else:
            result += ch

    return result


def generate_suggestions(password):

    suggestions = []

    special = "@#$%&!"
    numbers = "123456789"

    # Suggestion 1
    s1 = alternate_case(password.replace("@", "")).replace("!", "")
    s1 += random.choice(numbers)
    s1 += "@"
    suggestions.append(s1)

    # Suggestion 2
    s2 = password.title().replace("@", "")
    s2 += str(random.randint(10, 99))
    s2 += random.choice(special)
    suggestions.append(s2)

    # Suggestion 3
    s3 = "".join(random.sample(password, len(password)))
    suggestions.append(s3)

    # Suggestion 4
    s4 = alternate_case(password)
    suggestions.append(s4)

    # Suggestion 5
    s5 = password[::-1]
    suggestions.append(s5)

    return suggestions


def main():

    password = input("Enter Password: ")

    strength, feedback = check_strength(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions to Improve:")
        for item in feedback:
            print("-", item)

    print("\nGenerated Password Suggestions:")

    suggestions = generate_suggestions(password)

    for i, pwd in enumerate(suggestions, start=1):
        print(f"{i}. {pwd}")


if __name__ == "__main__":
    main()