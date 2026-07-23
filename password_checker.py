import random

# -------------------------------
# Password Suggestion Generator
# -------------------------------
def generate_suggestions(password):
    suggestions = []

    # Reverse digits
    digits = ''.join(c for c in password if c.isdigit())
    letters = ''.join(c for c in password if c.isalpha())
    specials = ''.join(c for c in password if not c.isalnum())

    if digits:
        suggestions.append(letters.capitalize() + specials + digits[::-1])

    # Alternate uppercase/lowercase
    alt = ""
    upper = True
    for ch in letters:
        if upper:
            alt += ch.upper()
        else:
            alt += ch.lower()
        upper = not upper

    if digits:
        shuffled_digits = ''.join(random.sample(digits, len(digits)))
    else:
        shuffled_digits = str(random.randint(100, 999))

    suggestions.append(alt + specials + shuffled_digits)

    # Random capitalization
    random_case = ""
    for ch in letters:
        random_case += ch.upper() if random.choice([True, False]) else ch.lower()

    random_special = specials if specials else "@"
    random_num = ''.join(str(random.randint(0, 9)) for _ in range(max(3, len(digits))))

    suggestions.append(random_case + random_special + random_num)

    return suggestions

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
        missing.append("❌ Minimum length of 8 characters")

    if has_upper:
        score += 1
    else:
        missing.append("❌ At least one uppercase letter")

    if has_lower:
        score += 1
    else:
        missing.append("❌ At least one lowercase letter")

    if has_digit:
        score += 1
    else:
        missing.append("❌ At least one number")

    if has_special:
        score += 1
    else:
        missing.append("❌ At least one special character")

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

    if missing:
        print("\nSuggestions to improve your password:")
        for item in missing:
            print("•", item)

    print("\nSuggested Passwords:")
    for p in generate_suggestions(password):
        print("->", p)


    if len(password) < 8 or strength == "Weak":
        print("\n ❌Password is too weak. Please try again.\n")
    else:
        print("\n ✅Password accepted!")
        break
    

