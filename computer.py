
import random
from game_logic import CHOICES

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return random.choice(CHOICES)
