import random
import string


def generate_password(length=15, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generate a password on the following critiea. 
    :param length: Length of the password
    :param use_uppercase: Includes the use of uppercase letter(A-Z)
    :param use_lowercase: Includes the use of lowercase letter(a-z)
    :param use_digits: Includes the use of digit (0-9)!
    :param use_specails: Includes the use of spcail characters(!@£$%^&*><?|:}"{)
    """

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation


    if not characters:
        raise ValueError("Please use at least one of the character that is required from you.")


    password =  ''.join(random.choice(characters) for _ in range(length))

    return password


def user_preferences(valueError=None):
    try:
        length = int(input('Please enter the length needed: '))
        if length <= 7:
            print("Please choose a password greater than 8.")
            return user_preferences()
    except ValueError:
        print('Please enter a valid INTEGER (whole number without decimals) for your password. ')
        return user_preferences()


    use_uppercase = input('Do you want to use a uppercase letter(Yes or No): ').lower() == 'yes'
    use_lowercase = input('Do you want to use a lowercase letter(Yes or No): ').lower() == 'yes'
    use_digits = input('Do you want to  use digits in your password(Yes or No): ').lower() == 'yes'
    use_special = input('Do you want to use special characters in your password(Yes or No): ').lower() == 'yes'

    return length, use_uppercase, use_lowercase, use_digits, use_special


def password_generator():
    print("\n Welcome to the password generator.")

    length, use_uppercase, use_lowercase, use_digits, use_special = user_preferences()

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Password Generated: {password}")

    except ValueError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    password_generator()

    




