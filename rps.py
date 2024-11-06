import random
from time import sleep
import os


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def bad_choice(arg):
    try:
        if arg <= 0:
            print("Can't play rounds less than 1 :<")
    except:
        print("I can't understand text :<")

    while True:
        try:
            r = int(input("Try again.\nSelect the number of rounds you'd like to play: "))
            if r < 0:
                print("Can't play a negative number of rounds :<")
                continue
            else:
                break
        except ValueError:
            print("I can't understand text :<")
            continue
    return r

def game(rounds):
    scores = {
        "You": 0,
        "Computer": 0,
    }
    i = 0
    while i < rounds:
        while True:
            try:
                player_choice = int(input(f"Round {i + 1}\nDo you want to choose 0-Rock, 1-Paper, or 2-Scissors?\n#"))
                if player_choice > 2:
                    print("Invalid choice. Only values between 0-2")
                    continue
                else:
                    break
            except ValueError:
                print("Only numbers between 0-2 are accepted.")
                continue
        images = [rock, paper, scissors]
        if player_choice > 2:
            print("Player choice is invalid")
        else:
            print("Player choice:")
            print(images[player_choice])

        # Generate Computer Choice and print it
        computer_choice = random.randint(0, 2)
        print("Computer choice:")
        print(images[computer_choice])

        game_result = [player_choice, computer_choice]
        if player_choice == computer_choice:
            print("It's a draw")
        elif game_result == [0, 2] or game_result == [1, 0] or game_result == [2, 1]:
            print("You win")
            scores["You"] += 1
        elif player_choice > 2:
            print("You typed and invalid number. You lose")
            scores["Computer"] += 1
        else:
            print("You lose")
            scores["Computer"] += 1


        i += 1
        print(f"Current Scores\nYOU: {scores['You']}\nCOMPUTER: {scores['Computer']}")
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Final Scores\nYOU: {scores['You']}\nCOMPUTER: {scores['Computer']}")
    if scores['You'] < scores['Computer']:
        print("You Lose. Better luck next time :>")
    elif scores['You'] > scores['Computer']:
        print("You Win! God gamer")
    else:
        print("It's a Draw. Boring")




if __name__ == "__main__":
    first_game = True
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        if first_game:
            rounds_choice = input("Welcome to the rock-paper-scissors game. Select the number of rounds you'd like to play: ")
        else:
            rounds_choice = input("Select the number of rounds you'd like to play: ")
        try:
            rounds_choice = int(rounds_choice)
            if rounds_choice <= 0:
                rounds_choice = bad_choice(rounds_choice)
        except:
            rounds_choice = bad_choice(rounds_choice)

        game(rounds_choice)
        first_game = False
        play_again = input("Play again? Y/N: ")
        if play_again.lower() == "y":
            print("Starting another game")
            sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thanks for playing :>\nGoodbye")
            break

# I shall fix this code now