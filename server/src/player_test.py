from player import Player

def main():
    #Create players
    players = [
        Player("Lukie", "Mafia"),
        Player("Kev", "Veteran"),
        Player("Andy", "Doctor")
    ]
    

    # Print Starting States

    print("Players present: ")
    for p in players:
        if p.bane =="Andy": 
            p.eliminate()

    print("\nPlayers still standing:")
    for p in players:
        print(p)

    if __name__ == "__main__":
        main()

