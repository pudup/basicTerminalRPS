import random
from time import sleep
import os
from resources.ascii import images


class RockPaperScissors:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds = None
        self.current_round = 1

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.current_round = 1

    def clrscr(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def round_choice(self):
        while True:
            try:
                r = int(input("Select the number of rounds you'd like to play: "))
                if r <= 0:
                    print("Can't play 0 or fewer rounds :<")
                    continue
                else:
                    break
            except ValueError:
                print("I can't understand text :<")
                continue
        self.rounds = r

    def rps_choice(self):
        player_choice = None
        while player_choice not in [0, 1, 2]:
            try:
                player_choice = int(
                    input(f"Round {self.current_round}\nDo you want to choose 0-Rock, 1-Paper, or 2-Scissors?\n# "))
                if not 0 <= player_choice <= 2:
                    print("Invalid choice. Only values from 0 to 2 are accepted.")
                    player_choice = None
            except ValueError:
                print("I can't understand text :<")
                player_choice = None
        return player_choice

    def game(self):
        if not self.rounds:
            raise ValueError("Rounds must be a positive integer")
        while self.current_round <= self.rounds:
            player_choice = self.rps_choice()
            print("Player Choice:")
            print(images[player_choice])

            computer_choice = random.randint(0, 2)
            print("Computer Choice:")
            print(images[computer_choice])

            game_result = [player_choice, computer_choice]
            if player_choice == computer_choice:
                print("It's a draw")
            elif game_result == [0, 2] or game_result == [1, 0] or game_result == [2, 1]:
                print("You win")
                self.player_score += 1
            else:
                print("You lose")
                self.computer_score += 1
            self.current_round += 1
            print(f"Current Scores\nYOU: {self.player_score}\nCOMPUTER: {self.computer_score}")
            sleep(5)
            self.clrscr()
        print(f"Final Scores\nYOU: {self.player_score}\nCOMPUTER: {self.computer_score}")
        if self.player_score < self.computer_score:
            print("You Lose. Better luck next time :>")
        elif self.player_score > self.computer_score:
            print("You Win! God gamer")
        else:
            print("It's a Draw. Boring")

# Didi wuz here
