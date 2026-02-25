import hashlib
import requests
import re

def password_strength(password: str):
    feedback = []
    score = 0
    length = len(password)

    if length < 8:
        feedback.append("Too short: use at least 8 characters.")
    elif length < 12:
        score += 1
        feedback.append("Decent length, but 12+ characters is better.")
    else:
        score += 2
        feedback.append("Good length (12+ characters).")

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    if has_lower:
        score += 1
    else:
        feedback.append("Add some lowercase letters.")
    if has_upper:
        score += 1
    else:
        feedback.append("Add some uppercase letters.")
    if has_digit:
        score += 1
    else:
        feedback.append("Add some digits.")
    if has_symbol:
        score += 1
    else:
        feedback.append("Add special characters.")

    if score <= 2:
        verdict = "Weak"
    elif score <= 4:
        verdict = "Medium"
    elif score == 5:
        verdict = "Strong"
    else:
        verdict = "Very Strong"

    return score, verdict, feedback


def check_pwned_password(password: str):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("API request failed.")

    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)

    return 0


def main():
    print("=== Password Strength + Leak API Checker ===")

    while True:
        password = input("\nEnter a password to test: ")

        # ---- Strength analysis ----
        score, verdict, feedback = password_strength(password)
        print("\n--- Strength Analysis ---")
        print(f"Score: {score} / 6")
        print(f"Verdict: {verdict}")
        if feedback:
            print("Suggestions:")
            for f in feedback:
                print(" -", f)

        # ---- HIBP check ----
        print("\n--- Breach Database Check (Online) ---")

        try:
            count = check_pwned_password(password)
            if count > 0:
                print(f"❌ WARNING: This password has appeared in {count:,} data breaches!")
                print("    → DO NOT USE THIS PASSWORD")
            else:
                print("✅ Good news! This password was NOT found in online breach databases.")
        except Exception as e:
            print("Error during API check:", e)

        # ---- Ask to check more ----
        choice = input("\nDo you want to check another password? (y/n): ").strip().lower()
        if choice != "y":
            print("\nExiting program. Stay safe! 🔐")
            break


if __name__ == "__main__":
    main()
