#
# Blackjack Objective game:
#

from random import*
# import os
#
#
# def cls():
#     os.system('cls' if os.name == 'nt' else 'clear')


# Class Deck:
class Deck:
    # Constructor of the class Deck:
    def __init__(self, name):
        self.name = name
        self.ace = 0
        self.game = True
        self.first_hit = False
        self.cards = ""
        self.sum = 0

    # Method that returns string of the cards on the table and sum of this cards:
    def score(self):
        return self.cards + " = " + str(self.sum)

    # Hit method:
    def hit(self):
        card = randint(2, 14)

        if self.first_hit:
            self.cards += " + "

        if card == 11:
            card = 10
            self.cards += "J(10)"
        elif card == 12:
            card = 10
            self.cards += "Q(10)"
        elif card == 13:
            card = 10
            self.cards += "K(10)"
        elif card == 14:
            card = 11
            self.cards += "A(11)"
            self.ace += 1
        else:
            self.cards += str(card)

        self.sum += card
        self.first_hit = True

    # Stand method:
    def stand(self):
        self.game = False

    # Checking:
    def result(self, deck2):
        if self.ace == 2:
            self.sum -= 1
            self.stand()
        elif self.sum > 21 and self.ace > 0:
            self.ace -= 1
            self.sum -= 10
        else:
            if self.sum == 21:
                self.stand()
            elif self.sum > 21:
                self.stand()
                deck2.stand()


# Artificial intelligence:
def ai(player1, player2):
    if not player1.game and player1.sum < player2.sum:
        player2.stand()
    elif player1.sum < player2.sum and player2.sum > 17:
        player2.stand()
    elif player1.sum == player2.sum and player2.sum >= 17:
        player2.stand()
    else:
        player2.hit()


# Print the score:
def game_print(player1, player2):
    print('\n-----------------------\n')
    print(player1.name + ":", player1.score())
    print(player2.name + ":", player2.score())
    print('\n-----------------------\n')


# Player picking decision:
def player_decision(player1, player2):
    if player1.game:
        decision = input('Take another card (hit or whatever) or stand (stand or stop): ').lower()

        if decision == "stop" or decision == "stand":
            player1.stand()
        else:
            player1.hit()
            player1.result(player2)
    else:
        print(player1.name, "does not play!")


# Check and print game result:
def game_result(player1, player2):
    game_print(player1, player2)
    if player1.ace == 2:
        print("Blackjack!", player1.name, "wins!")
    elif player2.ace == 2:
        print("Blackjack!", player2.name, "wins!")
    elif player1.sum > player2.sum:
        if player1.sum < 22:
            print(player1.name, "wins!")
        else:
            print(player2.name, "wins!")
    elif player2.sum > player1.sum:
        if player2.sum < 22:
            print(player2.name, "wins!")
        else:
            print(player1.name, "wins!")
    else:
        print("Tie!")


# Game for 1 player:
def game_1p():
    game = True
    player1 = Deck("Player")
    player2 = Deck("Computer")
    player1.hit()
    player1.hit()
    player2.hit()
    player1.result(player2)
    while game:
        game_print(player1, player2)
        player_decision(player1, player2)

        if player2.game:
            print(player2.name, "draws a card!")
            ai(player1, player2)
            player2.result(player1)
        else:
            print(player2.name, "does not play!")

        if not player1.game and not player2.game:
            game = False
            game_result(player1, player2)


# Game for 2 players:
def game_2p():
    game = True
    player1 = Deck("Player 1")
    player2 = Deck("Player 2")
    player1.hit()
    player1.hit()
    player2.hit()
    player2.hit()
    player1.result(player2)
    player2.result(player1)
    while game:
        game_print(player1, player2)
        print(player1.name, "turn:")
        player_decision(player1, player2)
        game_print(player1, player2)
        print(player2.name, "turn:")
        player_decision(player2, player1)

        if not player1.game and not player2.game:
            game = False
            game_result(player1, player2)


# Main:
run = True
while run:
    print('\n-----------------------\n')
    print("1 - game for 1 player (player vs. computer)")
    print("2 - game for 2 players (player1 vs. player2)")
    print("3 - exit the game\n")
    what = input("What you choose: ")

    if what == "1":
        game_1p()
        # run = False
    elif what == "2":
        game_2p()
        # run = False
    elif what == "3":
        run = False
    else:
        print("Nope! That's not a valid value.")
