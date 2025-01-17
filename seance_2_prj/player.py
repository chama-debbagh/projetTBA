class Player:

    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.health = 100  # Ajout d'un système de santé

    def move(self, direction):
        if self.current_room:
            self.history.append(self.current_room.name)

        if not self.current_room:  # Vérifie si le joueur n'est pas dans une pièce
            print("Erreur : Vous n'êtes dans aucune pièce. Déplacez-vous pour commencer.")
            return False


        next_room = self.current_room.get_exit(direction)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        if next_room.puzzle and not next_room.puzzle_solved:
            print("\nVous devez résoudre l'énigme avant de continuer. Entrer solve .\n")
            return False

        self.current_room = next_room
        print(self.current_room.get_long_description())
        self.print_history()
        return True

    def print_history(self):
        if self.history:
            print("Vous avez visité les pièces suivantes :")
            for room_name in self.history:
                print(f"  - {room_name}")
        else:
            print("Vous n'avez pas encore visité de pièces.")

    def add_item_to_inventory(self, item):
        self.inventory[item.name] = item

    def remove_item_from_inventory(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Vous avez retiré '{item_name}' de votre inventaire.")
        else:
            print(f"'{item_name}' n'est pas dans votre inventaire.")

    def adjust_health(self, amount):
        self.health += amount
        if self.health <= 0:
            print(f"{self.name} a succombé à la peur. Fin du jeu.")
        else:
            print(f"Santé restante : {self.health}")

    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."
        inventory_description = "\nObjets dans votre inventaire :\n"
        for item in self.inventory.values():
            inventory_description += f"  - {item.name}: {item.description} ({item.weight} kg)\n"
        return inventory_description
