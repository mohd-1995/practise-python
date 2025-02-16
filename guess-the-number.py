import random

def guess_the_number():
    number_to_guess = random.randint(1,100)
    attempts = 0

    print('Welcome to the number guessing number.')
    print('Guess the number between 1 and 100.')

    while True:
        try:
            guess = int(input('Please enter your guess: '))
        except ValueError:
            print('Please enter a valid number, try again.')


        attempts += 1

        if guess < number_to_guess:
            print('Your guess is too low. Please try again...')
            continue

        elif guess > number_to_guess:
            print('Your guess is too high. Please try again...')

        else:
            print(f'Congrattsss! You guess the right number in {attempts} attempts.')
            break


if __name__ == "__main__":
    guess_the_number()