from item import Item

# Define the Room class.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Dictionnaire des sorties possibles
        self.exit_puzzles = {}  # Dictionnaire des énigmes pour chaque sortie
        self.exit_solutions = {}  # Dictionnaire des solutions pour chaque sortie
        self.exit_puzzles_solved = {}  # Dictionnaire pour suivre les énigmes résolues
        self.items = set()  # Objets dans la pièce (si nécessaire)

    def get_exit(self, direction):
        """
        Retourne la pièce associée à une direction donnée.
        """
        return self.exits.get(direction)

    def get_exit_string(self):
        """
        Retourne une chaîne de caractères listant toutes les sorties possibles.
        """
        exit_string = "Sorties disponibles :\n"
        for exit, room in self.exits.items():
            exit_string += f"  - {exit} : {room.name}\n"
        return exit_string.strip()

    def get_long_description(self):
        """
        Retourne une description complète de la pièce, incluant les sorties et les objets.
        """
        description = f"\nVous êtes {self.description}\n"
        description += self.get_exit_string()
        if self.items:
            description += f"\nObjets dans la pièce :\n  - {', '.join(str(item) for item in self.items)}"
        return description

    def add_exit_puzzle(self, direction, puzzle, solution):
        """
        Ajoute une énigme à une sortie spécifique.
        """
        self.exit_puzzles[direction] = puzzle
        self.exit_solutions[direction] = solution
        self.exit_puzzles_solved[direction] = False

    def solve_exit_puzzle(self, direction, attempt):
        """
        Résout l'énigme d'une sortie donnée.
        """
        if direction in self.exit_puzzles_solved and self.exit_puzzles_solved[direction]:
            print("Cette énigme a déjà été résolue.")
            return True

        if direction in self.exit_solutions and attempt.lower() == self.exit_solutions[direction].lower():
            self.exit_puzzles_solved[direction] = True
            print("Bravo ! Vous avez résolu l'énigme.")
            return True
        else:
            if direction not in self.exit_solutions:
                print(f"Erreur : aucune énigme n'est définie pour la sortie '{direction}'.")
            else:
                print("Ce n'est pas la bonne réponse. Essayez encore.")
            return False

    def add_item(self, item):
        """
        Ajoute un objet à la pièce.
        """
        self.items.add(item)

    def remove_item(self, item):
        """
        Retire un objet de la pièce.
        """
        self.items.discard(item)

# Exemple d'utilisation (test local uniquement)
if __name__ == "__main__":
    test_room = Room("Test Room", "Description de test")
    test_room.add_exit_puzzle("N", "Quelle est la capitale de la France ?", "Paris")
    print(test_room.exit_puzzles)
    print(test_room.exit_solutions)
