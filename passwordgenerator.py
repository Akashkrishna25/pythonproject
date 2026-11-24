
import string
import secrets


def generate_password(length, upper, lower, digits, symbols):

    characters = ""
    password = []

    if upper:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if lower:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not characters:
        return "Error: Select at least one character type!"

    if length < len(password):
        return "Error: Password length is too short!"

    for i in range(length - len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():

    print("===== PASSWORD GENERATOR =====")

    while True:

        try:
            length = int(input("\nEnter password length: "))

            if length <= 0:
                print("Length must be greater than zero!")
                continue

            upper = input("Include uppercase? (y/n): ").lower() == "y"

            lower = input("Include lowercase? (y/n): ").lower() == "y"

            digits = input("Include numbers? (y/n): ").lower() == "y"

            symbols = input("Include symbols? (y/n): ").lower() == "y"

            password = generate_password(
                length, upper, lower, digits, symbols
            )

            print("\nGenerated Password:", password)

        except ValueError:
            print("Please enter a valid number!")
            continue

        again = input("\nGenerate another password? (y/n): ")

        if again.lower() != "y":
            print("Thank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()
