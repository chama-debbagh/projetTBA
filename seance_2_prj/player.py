class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []  # Pour suivre les déplacements du joueur
        self._inventory = {}

    def move(self, direction):
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            self.history.append(self.current_room)
            self.current_room = next_room
            print(f"\nVous êtes maintenant dans {self.current_room.name}.")
        else:
            print("\nIl n'y a pas de sortie dans cette direction.")

    def get_inventory(self):
        if not self._inventory:
            return "\nVotre inventaire est vide."
        else:
            inventory_list = "\nVous avez dans votre inventaire :\n"
            for item in self._inventory.values():
                inventory_list += f"  - {item}\n"
            return inventory_list

    def add_item_to_inventory(self, item):
        self._inventory[item.name] = item
        print(f"\nVous avez ajouté {item.name} à votre inventaire.")

    def remove_item_from_inventory(self, item_name):
        if item_name in self._inventory:
            removed_item = self._inventory.pop(item_name)
            print(f"\nVous avez retiré {removed_item.name} de votre inventaire.")
        else:
            print(f"\nL'objet {item_name} n'est pas dans votre inventaire.")
