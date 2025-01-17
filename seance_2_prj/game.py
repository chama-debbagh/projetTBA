from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

   # directions = set(["N", "E", "S", "O", "U", "D"])
class Game:
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.player = None
        self.game_state = "playing"  # Can be "playing", "won", or "lost"

    def setup(self):
        # Création des énigmes
        riddles = [
            Riddle("Je te suis partout. Je disparais chaque fois que la lumière arrive. Qui suis-je ?", "ombre"),
            Riddle("Je monte et je descends, mais je ne bouge jamais. Qui suis-je ?", "escaliers"),
            Riddle("Combien font 12 divisé par 3, multiplié par 2 ?", "8"),
            Riddle("Plus j'ai de gardiens, moins je suis gardé. Moins j'ai de gardiens, plus je suis gardé. Qui suis-je ?", "secret")
        ]

        # Création des pièces
        hall = Room("Hall d'entrée", "un hall sombre et poussiéreux", riddles[0])
        salon = Room("Salon", "une pièce avec des meubles recouverts de draps blancs", riddles[1])
        cuisine = Room("Cuisine", "une cuisine abandonnée avec des ustensiles rouillés", riddles[2])
        bibliotheque = Room("Bibliothèque", "une vaste bibliothèque aux étagères couvertes de toiles d'araignées", riddles[3])

        # Configuration des sorties
        hall.exits = {"N": salon, "E": cuisine, "O": bibliotheque}
        salon.exits = {"S": hall, "E": bibliotheque}
        cuisine.exits = {"O": hall, "N": bibliotheque}
        bibliotheque.exits = {"S": cuisine, "E": salon}

        self.rooms = [hall, salon, cuisine, bibliotheque]
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = hall

    def play(self):
        self.setup()
        print(f"\nBienvenue {self.player.name} dans la maison hantée!")
        print("Votre mission : explorez chaque pièce et résolvez les énigmes pour découvrir les secrets de la maison et gagner.")
        print("\nCommandes disponibles:")
        print("- 'go [direction]' pour vous déplacer (N, S, E, O)")
        print("- 'quit' pour quitter le jeu")
        print(self.player.current_room.get_long_description())

        while not self.finished:
            command = input("\nQue voulez-vous faire? > ").lower().split()
            
            if not command:
                continue
                
            if command[0] == "quit":
                print("Au revoir!")
                self.finished = True
            elif command[0] == "go" and len(command) > 1:
                result = self.player.move(command[1].upper())
                if result == "win":
                    self.finished = True
                    self.game_state = "won"
                elif result == "lose":
                    self.finished = True
                    self.game_state = "lost"
            else:
                print("Commande non reconnue. Utilisez 'go [direction]' ou 'quit'.")

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()