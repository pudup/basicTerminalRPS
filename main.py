from game import RockPaperScissors
from time import sleep

if __name__ == "__main__":
    keep_playing = True
    rps = RockPaperScissors()
    while keep_playing:
        rps.clrscr()
        print("Welcome to the rock-paper-scissors game")
        rps.round_choice()
        rps.game()
        play_again = input("Play again? Y/N: ")
        if play_again.lower() == "y":
            print("Starting another game")
            sleep(5)
            rps.reset()
            rps.clrscr()
        else:
            rps.clrscr()
            print("Thanks for playing :>\nGoodbye")
            keep_playing = False
