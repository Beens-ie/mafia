# Player class and roles


class Player: 
    def __init__(self, name: str, role: str):
        self.name = name # Name of player
        self.role = role # Role of player
        self.alive = True # Player Alive Status

    def eliminate(self):
        # Marks player as eliminated
        self.alive = False

    def assign_role(self, role):
        self.role = role


    def __str__(self):
        # Nicely formats player information
        status = "Alive" if self.alive else "Dead and gone"
        return f"{self.name} - {self.role} ({status})"

