# Game state, phase transitions, win conditions

# game_manager.py

from player import Player
import random

class GameManager:
    def __init__(self):
        self.players = []
        self.day_count = 1
        self.i_night = False
        self.game_over = False

    def start_game(self):
        print("Game Started!")
        self.assign_roles()
        self.print_players()

    def assign_roles(self):
        #Randomly assign x mafia and x town from pool
        #add in scaling logic for selection
        roles = ["Mafia"] + ["Town"] * (len(self.players) - 1)
        random.shuffle(roles)
        #return to this for role assignment priorities

        for player, role in zip(self.players, roles):
            player.assign_role(role)

    def print_players(self):
        for p in self.players:
            print(p)

    def next_plase(self):
        self.is_night = not self.is_night
        if self.is_night: 
            print(f"Night {self.day_count}...")

        else:
            print(f"Day {self.day_count} begins..")
            self.day_count += 1

    def check_game_over(self):
        #Define Game-end logic here. Maybe replace later with another readable file that is affected + updated as day event runs 
        #define maf / town alive keeping game running
        mafia = [p for p in self.players if p.role == "Mafia" and p.alive] # Adjust for special rules ie. witch when added
        town = [p for p in self.players if p.role != "mafia" and p.alive]
        if not mafia:
            self.game_over = True
            print("Town wins!")

        elif len(mafia) >= len(town):
            self.game_over = True
            print("Maf wins!")