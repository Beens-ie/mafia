# Game state, phase transitions, win conditions

# game_manager.py

from player import Player

class GameManager:
    def __init__(self):
        self.players = []
        self.day_count = 1

    def setup_sample_game(self):
        """Setup a few players for testing purposes."""
        self.players = [
            Player("Lukie", "Mafia"),
            Player("Kev", "Veteran"),
            Player("Andy", "Doctor")
        ]

    def run_sample_day(self):
        """Simulate a day and a night round."""
        print(f"\nDay {self.day_count} begins")
        for p in self.players:
            print(p)

        print("\nNight falls... someone dies!")
        for p in self.players:
            if p.name == "Andy":
                p.eliminate()

        print("\nMorning arrives...")
        for p in self.players:
            print(p)

        self.day_count += 1
