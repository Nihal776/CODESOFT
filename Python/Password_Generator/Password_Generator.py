import random
import string

def generate_password(length=12):
    """Generates a password with at least one uppercase, lowercase, and special character."""
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        if (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

def main():
    password = generate_password(12)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
