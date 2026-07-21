#Password Strength Checker
def check_strength(password):
    score = 0
    missing = []

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if len(password) >= 8:
        score += 1
    else:
        missing.append("Minimum length of 8 characters")

    if has_upper:
        score += 1
    else:
        missing.append("At least one uppercase letter")

    if has_lower:
        score += 1
    else:
        missing.append("At least one lowercase letter")

    if has_digit:
        score += 1
    else:
        missing.append("At least one number")

    if has_special:
        score += 1
    else:
        missing.append("At least one special character")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, missing


#MAIN PROGRAM
while True:
    password = input("Enter your password: ")

    strength, missing = check_strength(password)

    print("\nPassword Strength:", strength)