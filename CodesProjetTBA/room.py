
from riddle import Riddle
class Room:
    """
    Classe représentant une pièce dans la maison hantée.
    """
    def __init__(self, name, description, riddle=None):
        self.name = name
        self.description = description
        self.exits = {}  # Dictionnaire des sorties {direction: Room}
        self.riddle = riddle
        self.solved = False
        self.inventory = []  # Liste des objets dans la pièce

    def get_exit(self, direction):
        """Retourne la pièce dans la direction donnée."""
        return self.exits.get(direction)

    def get_exit_string(self):
        """Retourne une chaîne décrivant les sorties disponibles."""
        exit_string = "Sorties disponibles: "
        exits = [direction for direction, room in self.exits.items() if room is not None]
        return exit_string + ", ".join(exits)

    def get_long_description(self):
        """Retourne une description détaillée de la pièce."""
        return f"\nVous êtes dans {self.name}. {self.description}\n{self.get_exit_string()}\n"


    def get_exit_string(self):
        exit_string = "Sorties disponibles: "
        #exit_string += ", ".join(self.exits.keys())
        #return exit_string or "Aucune sortie disponible."
        exits = [direction for direction, room in self.exits.items() if room is not None]
        return exit_string + ", ".join(exits)


    def get_long_description(self):
        return f"\nVous êtes {self.name}. {self.description}\n{self.get_exit_string()}\n"

    #def add_exit(self, direction, room):
       # self.exits[direction] = room
