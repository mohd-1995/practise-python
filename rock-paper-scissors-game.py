import random


def the_computer_choice():
    choices = ['paper', 'rock', 'scissors']
    return random.choice(choices)


def the_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input('Please enter your choice (rock, paper, scissors): ').lower()

    # Validate user input
    while user_input not in choices:
        print('Invalid choice!!')
        user_input = input('Please enter your choice (rock, paper, scissors): ').lower()

    return user_input


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        print('You win !!! YOU are the WINNER!!')
    else:
        print('Computer wins !! AHAHAHA!!')


def play_game():
    print('Welcome to my rock, paper, scissors game! And GOODLUCK!!')
    user_choice = the_user_choice()
    computer_choice = the_computer_choice()
    print(f'You chose: {user_choice}')
    print(f'The computer chose: {computer_choice}')
    determine_winner(user_choice, computer_choice)


if __name__ == "__main__":
    play_game()