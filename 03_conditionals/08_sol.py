# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif 6 <= len(password) <= 10:
        return "Medium"
    else:
        return "Strong"

# Example usage:
password = input("Enter your password: ")

strength = check_password_strength(password)
print("Your password strength is:", strength)
