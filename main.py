
from player import get_player_choice, ask_play_again
from computer import get_computer_choice
from game_logic import check_winner, get_result_message
from scoreboard import Scoreboard

def display_banner():
    """Prints the game title banner."""
    print("================================")
    print("   ROCK  |  PAPER  |  SCISSORS  ")
    print("================================")

def play_round(scoreboard):
    """Plays a single round of the game."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose    : {player_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = check_winner(player_choice, computer_choice)
    message = get_result_message(player_choice, computer_choice, winner)

    print(f"\n>> {message}")
    scoreboard.update(winner)
    scoreboard.display()

def main():
    display_banner()
    print("Welcome! Let's play Rock Paper Scissors!\n")

    scoreboard = Scoreboard()

    while True:
        play_round(scoreboard)
        if not ask_play_again():
            break

    print("\n" + scoreboard.get_final_result())
    print("\nThanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    main()
