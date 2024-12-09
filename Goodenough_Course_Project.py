import string
import time
import random


def is_password_valid(password):
    # Check if the password length is at least 16 characters
    if len(password) < 16:
        return False

    # Count the number of lowercase letters in the password
    lower_count = sum(1 for c in password if c in string.ascii_lowercase)
    # Count the number of uppercase letters in the password
    upper_count = sum(1 for c in password if c in string.ascii_uppercase)
    # Count the number of digits in the password
    digit_count = sum(1 for c in password if c in string.digits)
    # Count the number of special characters in the password
    special_count = sum(1 for c in password if c in string.punctuation)

    # Check if the password meets all complexity requirements
    return (lower_count >= 3 and
            upper_count >= 3 and
            digit_count >= 3 and
            special_count >= 3)


def encrypt_password(password):
    # Function to encrypt the password by shifting characters
    encrypted_chars = []
    for char in password:
        # Generate a random shift between -4 and 4
        shift = random.randint(-4, 4)
        # Apply the shift to the character's ASCII value
        new_char = chr(ord(char) + shift)
        # Add the shifted character to the result list
        encrypted_chars.append(new_char)
    # Join the list of characters into a single string
    encrypted_password = ''.join(encrypted_chars)

    # Function to convert each character to hexadecimal representation
    hex_password = ''.join([hex(ord(c))[2:] for c in encrypted_password])
    return hex_password


def create_user():
    # Prompt user to enter a username
    user_id = input("Enter your desired userID: ")
    print(f"Creating user with name, ID: {user_id}")

    # Prompt user to enter a password until it meets complexity requirements
    while True:
        password = input(
            "Your password...choose carefully. (16 characters long, min of 3 each - numbers, upper, lower, special): ")
        if is_password_valid(password):
            print("Welcome to the Matrix.")  # Indicate successful password setup
            break
        else:
            print("The price is wrong....Bob!")  # Indicate an invalid password

    # Display the entered userID and password
    print(f"UserID: {user_id}")
    print(f"Password: {password}")

    # Countdown for encryption
    for i in range(5, 0, -1):
        print(f"Encrypting in {i}...")
        time.sleep(1)  # Pause for 1 second between counts

    # Encrypt the password with random shifting and convert to hexadecimal
    hex_encrypted_password = encrypt_password(password)

    # Display the hexadecimal encrypted password
    print(f"Your password has been scrambled and smothered: {hex_encrypted_password}")


# Entry point for the program
if __name__ == "__main__":
    create_user()
