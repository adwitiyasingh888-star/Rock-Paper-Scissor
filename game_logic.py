
CHOICES = ["rock", "paper", "scissors"]

WINNING_COMBOS = {
    "rock": "scissors",  
    "paper": "rock",     
    "scissors": "paper"  
}

def check_winner(player_choice, computer_choice):
    """
    Determines the winner of a round.
    Returns: 'player', 'computer', or 'tie'
    """
    if player_choice == computer_choice:
        return "tie"
    elif WINNING_COMBOS[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def get_result_message(player_choice, computer_choice, winner):
    """Returns a human-readable result message."""
    if winner == "tie":
        return f"It's a tie! Both chose {player_choice}."
    elif winner == "player":
        return f"You win! {player_choice.capitalize()} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {player_choice}."
