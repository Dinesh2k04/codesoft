import random, string
def generate_password(length):
    give_char = string.ascii_letters + string.digits + string.punctuation
    Password = ''.join(random.choice(give_char) for _ in range(length))
    return Password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("Password length must be greater than 1 ")
        passcode = generate_password(length)
        print("System Generated Password:", passcode)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
