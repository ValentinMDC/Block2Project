import re

def check_password_strength(password: str) -> dict:
    score = 0

    # Rule 1: At least 10 characters
    if len(password) >= 10:
        score += 5

    # Rule 2: Contains both letters and numbers
    if re.search(r"[A-Za-z]", password) and re.search(r"\d", password):
        score += 5

    # Rule 3: Contains at least one uppercase letter
    if re.search(r"[A-Z]", password):
        score += 5

    # Determine strength
    if score == 15:
        strength = "Strong"
    elif score == 10:
        strength = "Moderate"
    elif score == 5:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {"score": score, "strength": strength}


# Example usage
if __name__ == "__main__":
    user_input = input("Enter password: ")
    check_password_strength(user_input)