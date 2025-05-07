#socket / websocket server code
#server.py

from player import Player

from game_manager import GameManager

def main():
    game = GameManager()
    game.setup_sample_game()
    game.run_sample_day()

if __name__ == "__main__":
    main()