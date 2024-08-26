import random
import string

def generate_password(length=12):
    # Define the character sets to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password (default is 12): ") or 12)
        
        if length < 6:
            print("Password length should be at least 6 characters for security.")
            return

        password = generate_password(length)
        print(f"Generated password: {password}")

    except ValueError:
        print("Please enter a valid number.")

# Run the password generator
main()