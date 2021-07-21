#
# Simple console game rock paper scissors:
#

from random import*
game = True

while game:
    player = (input("rock/paper/scissors: ")).lower()
    rand = randint(1, 3)

    if rand == 1:
        print("rock")
        if player == "rock":
            print("Tie!")
        elif player == "paper":
            print("You win!")
        elif player == "scissors":
            print("You lose!")

    elif rand == 2:
        print("paper")
        if player == "rock":
            print("You lose!")
        elif player == "paper":
            print("Tie!")
        elif player == "scissors":
            print("You win!")

    elif rand == 3:
        print("scissors")
        if player == "rock":
            print("You win!")
        elif player == "paper":
            print("You lose!")
        elif player == "scissors":
            print("Tie!")

    if player != "rock" and player != "paper" and player != "scissors":
        print("It is invalid word! Rock, paper or scissors!")
    else:
        player = input("You want to play again? (yes or no): ").lower()
        if player == "yes":
            game = True
        else:
            game = False
