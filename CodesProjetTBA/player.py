from PnjGUI import PnjGUI
# player.py
class Player:
    """
    Classe représentant le joueur.
    """
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.points = 0
        self.wrong_attempts = 0
        self.max_wrong_attempts = 3
        self.history = []  # Liste des pièces visitées
        self._inventory = {}  # Inventaire du joueur

    def move(self, direction):
        """Déplace le joueur dans la direction spécifiée."""
        next_room = self.current_room.get_exit(direction)
        
        if next_room is None:
            print("\nIl n'y a pas de porte dans cette direction!\n")
            return False

        # Ajoute la pièce actuelle à l'historique avant de se déplacer
        if self.current_room:
            self.history.append(self.current_room.name)
        
        if not next_room.solved and next_room.riddle:
            print(f"\nÉnigme pour entrer dans {next_room.name}:")
            print(next_room.riddle.question)
            answer = input("Votre réponse: ")
            
            if next_room.riddle.check_answer(answer):
                print("\nBonne réponse! Vous gagnez un point.")
                next_room.solved = True
                self.points += 1
                self.current_room = next_room
                print(self.current_room.get_long_description())
                self.print_history()  # Affiche l'historique après chaque déplacement
                
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

    def print_history(self):
        """Affiche l'historique des pièces visitées."""
        if self.history:
            print("\nPièces visitées:")
            for room in self.history:
                print(f"    - {room}")
        else:
            print("\nVous n'avez pas encore visité de pièces.")

    def get_inventory(self):
        """Retourne le contenu de l'inventaire."""
        if not self._inventory:
            return "\nVotre inventaire est vide."
        inventory_str = "\nVotre inventaire contient:"
        for item in self._inventory.values():
            inventory_str += f"\n    - {item.name}: {item.description}"
        return inventory_str