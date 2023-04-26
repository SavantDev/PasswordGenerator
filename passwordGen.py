import random
import string

# Defines the password generator function
def generate_password(length=12, include_digits=True, include_symbols=True):
    # Define the character sets to use
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits if include_digits else ""
    symbols = string.punctuation if include_symbols else ""

    # Combine the character sets based on the user's preferences
    valid_chars = uppercase_letters + lowercase_letters + digits + symbols

    # Generate the password
    password = "".join(random.choice(valid_chars) for _ in range(length))

    return password

# Prompts the user for their password preferences
print("Welcome to the password generator!")
length = int(input("How many characters should the password be? "))
include_digits = input("Should the password include digits? (y/n) ").lower() == "y"
include_symbols = input("Should the password include symbols? (y/n) ").lower() == "y"

# Generates and prints the password
password = generate_password(length, include_digits, include_symbols)
print(f"Your password is: {password}")
