from player import Player
from room import Room
from riddle import Riddle
from command import Command

class Game:
    """
    Classe principale du jeu.
    """
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.player = None
        self.game_state = "playing"
        self.commands = {}
        self.directions = set(["N", "E", "S", "O" , "D" , "U"])

    def setup(self):
        """Configure le jeu avec les pièces et les énigmes."""
        # Création des énigmes
        riddles = [
            Riddle("Je te suis partout. Je disparais chaque fois que la lumière arrive. Qui suis-je ?", "ombre"),
            Riddle("Je monte et je descends, mais je ne bouge jamais. Qui suis-je ?", "escaliers"),
            Riddle("Combien font 12 divisé par 3, multiplié par 2 ?", "8"),
            Riddle("Plus j'ai de gardiens, moins je suis gardé. Moins j'ai de gardiens, plus je suis gardé. Qui suis-je ?", "secret"),
            Riddle("Je peux monter jusqu'au ciel mais je ne peux pas voler. Qui suis-je ?", "fumee"),
            Riddle("Dans une cave sombre, on me trouve souvent pleine. Qui suis-je ?", "bouteille")
        ]

        # Création des pièces du rez-de-chaussée
        hall = Room("Hall d'entrée", "un hall sombre et poussiéreux", riddles[0])
        salon = Room("Salon", "une pièce avec des meubles recouverts de draps blancs", riddles[1])
        cuisine = Room("Cuisine", "une cuisine abandonnée avec des ustensiles rouillés", riddles[2])
        bibliotheque = Room("Bibliothèque", "une vaste bibliothèque aux étagères couvertes de toiles d'araignées", riddles[3])


        # Création des pièces de l'étage
        grenier = Room("Grenier", "un grenier poussiéreux rempli d'objets anciens", riddles[4])
        chambre = Room("Chambre", "une chambre avec un vieux lit à baldaquin", None)


        # Création des pièces du sous-sol
        cave = Room("Cave", "une cave humide avec des toiles d'araignées", riddles[5])
        laboratoire = Room("Laboratoire", "un ancien laboratoire secret", None)




        
        # Configuration des sorties du rez-de-chaussée
        hall.exits = {
            "N": salon, 
            "E": cuisine, 
            "O": bibliotheque,
            "U": None,  # On ne peut pas monter depuis le hall
            "D": cave   # On peut descendre à la cave
        }

        salon.exits = {
            "S": hall, 
            "E": bibliotheque,
            "U": chambre,  # On peut monter à la chambre
            "D": None
        }

        cuisine.exits = {
            "O": hall, 
            "N": bibliotheque,
            "U": None,
            "D": laboratoire  # On peut descendre au laboratoire
        }

        bibliotheque.exits = {
            "S": cuisine, 
            "E": salon,
            "U": grenier,  # On peut monter au grenier
            "D": None
        }

        # Configuration des sorties de l'étage
        grenier.exits = {
            "D": bibliotheque,  # On peut descendre à la bibliothèque
            "N": None,
            "S": None,
            "E": None,
            "O": None,
            "U": None
        }

        chambre.exits = {
            "D": salon,  # On peut descendre au salon
            "N": None,
            "S": None,
            "E": None,
            "O": None,
            "U": None
        }

        # Configuration des sorties du sous-sol
        cave.exits = {
            "U": hall,  # On peut monter au hall
            "N": None,
            "S": None,
            "E": laboratoire,
            "O": None,
            "D": None
        }

        laboratoire.exits = {
            "U": cuisine,  # On peut monter à la cuisine
            "N": None,
            "S": None,
            "E": None,
            "O": cave,
            "D": None
        }

        self.rooms = [hall, salon, cuisine, bibliotheque, grenier, chambre, cave, laboratoire]
        

        
        # Configuration des commandes
        self.commands = {
            "go": Command("go", " <direction> : se déplacer (N, S, E, O, U, D)", self.do_go, 1),
            "quit": Command("quit", " : quitter le jeu", self.do_quit, 0),
            "help": Command("help", " : afficher l'aide", self.do_help, 0),
            "look": Command("look", " : observer la pièce", self.do_look, 0)
        }

        # Création du joueur
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = hall

    def do_go(self, args):
        """Gère la commande 'go'."""
        if len(args) < 2:
            print("\nOù voulez-vous aller? Utilisez N, S, E, O, D ou U")
            return False
        return self.player.move(args[1].upper())

    def do_quit(self, args):
        """Gère la commande 'quit'."""
        print("\nAu revoir!")
        return "quit"

    def do_help(self, args):
        """Affiche l'aide du jeu."""
        print("\nCommandes disponibles:")
        for cmd in self.commands.values():
            print(f"- {cmd.command_word}{cmd.help_string}")
        return True

    def do_look(self, args):
        """Observe la pièce actuelle."""
        print(self.player.current_room.get_long_description())
        return True

    def play(self):
        """Démarre et gère la partie."""
        self.setup()
        print(f"\nBienvenue {self.player.name} dans la maison hantée!")
        print("Votre mission : explorez chaque pièce et résolvez les énigmes pour découvrir les secrets de la maison et gagner.")
        self.do_help([])
        print(self.player.current_room.get_long_description())

        while not self.finished:
            command = input("\nQue voulez-vous faire? > ").lower().split()
            
            if not command:
                continue
                
            cmd_word = command[0]
            if cmd_word in self.commands:
                result = self.commands[cmd_word].action(command)
                if result == "quit":
                    self.finished = True
                elif result == "win":
                    print("\nFélicitations! Vous avez gagné!")
                    self.finished = True
                elif result == "lose":
                    print("\nGame Over! Vous avez perdu.")
                    self.finished = True
            else:
                print("\nCommande non reconnue. Tapez 'help' pour voir les commandes disponibles.")

if __name__ == "__main__":
    game = Game()
    game.play()