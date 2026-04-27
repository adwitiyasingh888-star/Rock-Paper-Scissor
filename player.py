
from game_logic import CHOICES

def get_player_choice():
    """
    Asks the player to enter their choice.
    Keeps asking until a valid choice is given.
    Returns the valid choice as a string.
    """
    print("\nChoices: rock, paper, scissors")
    while True:
        choice = input("Your choice: ").strip().lower()
        if choice in CHOICES:
            return choice
        else:
            print(f"Invalid choice '{choice}'. Please type rock, paper, or scissors.")

def ask_play_again():
    """Asks the player if they want to play another round."""
    while True:
        answer = input("\nPlay again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please type 'yes' or 'no'.")
