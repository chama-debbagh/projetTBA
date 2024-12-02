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
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        
        # New rooms
        garden = Room("Garden", "dans un jardin luxuriant rempli de fleurs colorées et d'arbustes soigneusement taillés.")
        library = Room("Library", "dans une bibliothèque silencieuse avec des étagères débordant de livres anciens.")
        kitchen = Room("Kitchen", "dans une cuisine chaleureuse où l'odeur de pain frais flotte dans l'air.")
        dungeon = Room("Dungeon", "dans un donjon sombre et humide, des chaînes pendent aux murs.")
        bridge = Room("Bridge", "sur un pont de pierre qui traverse une rivière tumultueuse.")
        attic = Room("Attic", "dans un grenier poussiéreux rempli de vieux coffres et de toiles d'araignée.")
        laboratory = Room("Laboratory", "dans un laboratoire avec des fioles bouillonnantes et des livres ouverts sur des expériences alchimiques.")
        throne_room = Room("Throne Room", "dans une salle du trône majestueuse ornée de tapisseries dorées et de chandeliers imposants.")
        
        # Add rooms to the list
        self.rooms.extend([forest, tower, cave, cottage, swamp, castle, garden, library, kitchen, dungeon, bridge, attic, laboratory, throne_room])

        # Create exits for rooms

        forest.exits = {"N": cave, "E": tower, "S": garden, "O": None}
        tower.exits = {"N": library, "E": attic, "S": kitchen, "O": forest}
        cave.exits = {"N": None, "E": library, "S": forest, "O": dungeon}
        cottage.exits = {"N": None, "E": None, "S": tower, "O": cave}
        swamp.exits = {"N": tower, "E": None, "S": None, "O": castle}
        castle.exits = {"N": throne_room, "E": swamp, "S": None, "O": None}
        garden.exits = {"N": forest, "E": kitchen, "S": None, "O": None}
        library.exits = {"N": None, "E": None, "S": tower, "O": cave}
        kitchen.exits = {"N": tower, "E": None, "S": None, "O": garden}
        dungeon.exits = {"N": cave, "E": None, "S": None, "O": None}
        bridge.exits = {"N": None, "E": throne_room, "S": None, "O": None}
        attic.exits = {"N": laboratory, "E": None, "S": None, "O": tower}
        laboratory.exits = {"N": None, "E": None, "S": attic, "O": None}
        throne_room.exits = {"N": None, "E": castle, "S": None, "O": bridge}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = garden

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
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
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
