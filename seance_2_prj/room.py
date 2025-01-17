from item import Item
# Define the Room class.
class Room:

    def __init__(self, name, description, puzzle=None, solution=None, danger_level=0):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = set()
        self.puzzle = puzzle
        self.solution = solution
        self.puzzle_solved = False
        self.danger_level = danger_level  # Ajout d'un niveau de danger

    def get_exit(self, direction):
        return self.exits.get(direction)

    def get_exit_string(self):
        exit_string = "Sorties : "
        for exit in self.exits.keys():
            exit_string += exit + ", "
        return exit_string.strip(", ")

    def get_long_description(self):
        description = f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
        if self.items:
            description += f"\nObjets dans la pièce :\n    - {', '.join(str(item) for item in self.items)}\n"
        if self.puzzle and not self.puzzle_solved:
            description += f"\nÉnigme : {self.puzzle}\n"
        return description

    def add_item(self, item):
        self.items.add(item)

    def remove_item(self, item):
        self.items.discard(item)

    def solve_puzzle(self, attempt):
        if self.solution and attempt.lower() == self.solution.lower():
            self.puzzle_solved = True
            print("Vous avez résolu l'énigme !")
        else:
            print("Ce n'est pas la bonne réponse. Essayez encore.")
