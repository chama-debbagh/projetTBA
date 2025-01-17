from item import Item

# Define the Room class.
class Room:
    def __init__(self, name, description, riddle):
        self.name = name
        self.description = description
        self.riddle = riddle
        self.exits = {}
        self.solved = False

    def get_exit(self, direction):
        return self.exits.get(direction)

    def get_exit_string(self):
        exit_string = "Sorties disponibles: "
        #exit_string += ", ".join(self.exits.keys())
        #return exit_string or "Aucune sortie disponible."
        exits = [direction for direction, room in self.exits.items() if room is not None]
        return exit_string + ", ".join(exits)


    def get_long_description(self):
        return f"\nVous êtes {self.name}.{self.description}\n{self.get_exit_string()\n}"

    #def add_exit(self, direction, room):
       # self.exits[direction] = room
