import random

print("Welcome to the rock-paper-scissors game!")

while True:
    player = input("Please choose rock (r), paper (p), or scissors (s): ")

    if player not in ['r', 'p', 's']:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(['r', 'p', 's'])
    if player == computer:
        print("It's a tie!")
    elif player == 'r' and computer == 's':
        print("You win! Rock beats scissors.")
    elif player == 'p' and computer == 'r':
        print("You win! Paper beats rock.")
    elif player == 's' and computer == 'p':
        print("You win! Scissors beats paper.")
    else:
        print("You lose! The computer chose " + computer)

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != 'yes':
        break

print("Thanks for playing!")