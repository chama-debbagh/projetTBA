class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.point=0
        self.wrong_attempts=0
        self.max_wrong_attempts=3 
        #self.history = []  # Pour suivre les déplacements du joueur
        #self._inventory = {}

    def move(self, direction):
        next_room = self.current_room.get_exit(direction)
        if next_room is None:
            print("\nIl n'y a pas de porte dans cette direction!\n")
            return False
        
        if not next_room.solved:
            print(f"\nÉnigme pour entrer dans {next_room.name}:")
            print(next_room.riddle.question)
            answer = input("Votre réponse: ")

            if next_room.riddle.check_answer(answer):
                print("\nBonne réponse! Vous gagnez un point.")
                next_room.solved = True
                self.points += 1
                self.current_room = next_room
                print(self.current_room.get_long_description())
                
                if self.points >= 3:
                    print("\nFélicitations! Vous avez gagné le jeu en résolvant 3 énigmes!")
                    return "win"
            else:
                self.wrong_attempts += 1
                remaining_attempts = self.max_wrong_attempts - self.wrong_attempts
                print(f"\nMauvaise réponse! Il vous reste {remaining_attempts} tentatives.")
                
                if self.wrong_attempts >= self.max_wrong_attempts:
                    print("\nGame Over! Vous avez épuisé toutes vos tentatives.")
                    return "lose"
                return False
        else:
            self.current_room = next_room
            print(self.current_room.get_long_description())
        return True


        
        """
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            self.history.append(self.current_room)
            self.current_room = next_room
            print(f"\nVous êtes maintenant dans {self.current_room.name}.")
        else:
            print("\nIl n'y a pas de sortie dans cette direction.") """

    #def get_inventory(self):
     #   if not self._inventory:
       #     return "\nVotre inventaire est vide."
     #   else:
      #      inventory_list = "\nVous avez dans votre inventaire :\n"
       #     for item in self._inventory.values():
        #        inventory_list += f"  - {item}\n"
         #   return inventory_list
"""
    def add_item_to_inventory(self, item):
        self._inventory[item.name] = item
        print(f"\nVous avez ajouté {item.name} à votre inventaire.")

    def remove_item_from_inventory(self, item_name):
        if item_name in self._inventory:
            removed_item = self._inventory.pop(item_name)
            print(f"\nVous avez retiré {removed_item.name} de votre inventaire.")
        else:
            print(f"\nL'objet {item_name} n'est pas dans votre inventaire.")
"""