
class Scoreboard:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.total_rounds = 0

    def update(self, winner):
        """Updates the score based on round winner."""
        self.total_rounds += 1
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1
        else:
            self.ties += 1

    def display(self):
        """Prints the current scoreboard."""
        print("\n--- Scoreboard ---")
        print(f"  You      : {self.player_score}")
        print(f"  Computer : {self.computer_score}")
        print(f"  Ties     : {self.ties}")
        print(f"  Rounds   : {self.total_rounds}")
        print("------------------")

    def get_final_result(self):
        """Returns the overall game winner message."""
        if self.player_score > self.computer_score:
            return "🎉 You won the game! Congratulations!"
        elif self.computer_score > self.player_score:
            return "💻 Computer won the game. Better luck next time!"
        else:
            return "🤝 The overall game is a tie!"
