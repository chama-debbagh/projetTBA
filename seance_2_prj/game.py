# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)

        #ajouter des lieux 
        grenier = Room("Grenier", "dans un grenier poussiéreux avec de vieilles malles et des toiles d'araignée partout.") 
        self.rooms.append(grenier) 
        sous_sol = Room("Sous-sol", "dans un sous-sol sombre et humide où des bruits étranges se font entendre.") 
        self.rooms.append(sous_sol) 
        jardin = Room("Jardin", "dans un joli jardin plein de fleurs colorées et d'arbres fruitiers.") 
        self.rooms.append(jardin)
        cuisine = Room("Cuisine", "dans une petite cuisine où il y a des plats qui mijotent et des odeurs délicieuses.")
        self.rooms.append(cuisine)

        # Create exits for rooms
        #ajout des commande up et down pour integrer les nouv lieu en faisant le lien avec les autres lieu qui etaient deja exista

        forest.exits = {"N": cave, "E": jardin, "S": castle, "O": None, "U": grenier, "D": None}
        tower.exits = {"N": cottage, "E": None, "S": None, "O": cuisine, "U": None, "D": sous_sol} 
        cave.exits = {"N": None, "E": cottage, "S": forest, "O": None , "U": None, "D": None} 
        cottage.exits = {"N": None, "E": None, "S": tower, "O": cave, "U": None, "D": None} 
        swamp.exits = {"N": tower, "E": None, "S": None , "O": castle, "U": None, "D": None}
        castle.exits = {"N": forest, "E": swamp, "S": jardin, "O": None, "U": None, "D": None} 
        jardin.exits = {"N": castle, "E": None, "S": cuisine, "O": forest, "U": None, "D": None} 
        cuisine.exits = {"N": jardin, "E": tower, "S": None, "O": None, "U": None, "D": None}  
        grenier.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": forest} 
        sous_sol.exits = {"N": None, "E": None, "S": None, "O": None, "U": tower, "D": None}
   

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print("\nCette commande est non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
