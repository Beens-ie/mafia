from game_manager import GameManager
from player import Player
import time

print(">>> LOADED: src/server.py")

def main():
    game = GameManager()

    # Add some test players
    game.players = [
        Player("Lukie", "Unassigned"),
        Player("Kev", "Unassigned"),
        Player("Andy", "Unassigned")
    ]

    game.start_game()

    # Simulate a few day/night cycles
    while not game.game_over:
        time.sleep(2)  # Pause to simulate time passing
        game.next_phase()
        game.check_game_over()

if __name__ == "__main__":
    main()