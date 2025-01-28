import random
import string

def generate_password(length=6, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    # Combine all selected character pools
    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character type must be selected!")

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_symbols = input("Include special symbols? (yes/no): ").lower() == "yes"

    try:
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
