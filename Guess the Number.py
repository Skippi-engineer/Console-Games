#
# Simple console game guess the number:
#

from random import randint

game = True
i = 0
rand = randint(1, 10)
print("Guess the number between 1 and 10 in 5 guesses:")

while game:
    i += 1
    guess = int(input("Take a guess: "))

    if 1 > guess or guess > 10:
        print("\nI am thinking of the number in between 1 and 10! Try again!")
        i -= 1
    elif i > 5:
        print("\nThe number I was thinking of was:", rand, "Good luck next time!")
        game = False
    elif guess > rand:
        print("\nYour guess is too high! You have", 5 - i, "tries! Try again!")
    elif guess < rand:
        print("\nYour guess is too low! You have", 5 - i, "tries! Try again!")
    else:
        print("\nCongratulations! You guessed the number in", i, "guesses!")
        game = False
