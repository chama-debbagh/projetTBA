from item import Item

# Define the Room class.
class Room:
    def __init__(self, name, description, riddle, answer):
        self.name = name
        self.description = description
        self.riddle = riddle
        self.answer = answer.lower()
        self.exits = {}
        self.visited = False

    def get_exit(self, direction):
        return self.exits.get(direction)

    def get_exit_string(self):
        exit_string = "Sorties : "
        exit_string += ", ".join(self.exits.keys())
        return exit_string or "Aucune sortie disponible."

    def get_long_description(self):
        return f"\nVous êtes {self.description}. {self.get_exit_string()}"

    def add_exit(self, direction, room):
        self.exits[direction] = room
