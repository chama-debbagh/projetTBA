from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Game:

    directions = set(["N", "E", "S", "O", "U", "D"])

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.health = 100  # Ajout d'un système de santé

    def setup(self):
        help_cmd = Command("help", " : Afficher l'aide", Actions.help, 0)
        self.commands["help"] = help_cmd
        quit_cmd = Command("quit", " : Quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit_cmd
        go_cmd = Command("go", " <direction> : Se déplacer", Actions.go, 1)
        self.commands["go"] = go_cmd
        solve_cmd = Command("solve", " : Résoudre l'énigme de la pièce", Actions.solve, 0)
        self.commands["solve"] = solve_cmd
        inspect_cmd = Command("inspect", " : Inspecter la pièce pour des indices", Actions.inspect, 0)
        self.commands["inspect"] = inspect_cmd

        hall = Room(
            "Hall",
            "Vous êtes dans le hall d'entrée de la maison hantée, avec des chandeliers vacillants.",
            "Quel est le mot de passe de l'entrée ?",
            "sésame"
        )

        salon = Room(
            "Salon",
            "Un vieux salon avec des portraits effrayants. Le feu de la cheminée est éteint.",
            "Comment rallumer le feu ?",
            "allumette"
        )

        cuisine = Room(
            "Cuisine",
            "Une cuisine poussiéreuse avec des couteaux rouillés sur la table.",
            "Quel ingrédient manque pour finir le plat ?",
            "sel"
        )

        grenier = Room(
            "Grenier",
            "Un grenier obscur rempli de toiles d'araignée et de vieilles boîtes.",
            "Combien de boîtes y a-t-il ?",
            "7"
        )

        hall.exits = {"N": salon}
        salon.exits = {"S": hall, "E": cuisine}
        cuisine.exits = {"W": salon, "U": grenier}
        grenier.exits = {"D": cuisine}

        self.rooms = [hall, salon, cuisine, grenier]

        self.player = Player(input("Entrez votre nom : "))
        self.player.current_room = hall

    def reduce_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("\nVous avez succombé à la peur. Fin du jeu !")
            self.finished = True
        else:
            print(f"\nVotre santé actuelle : {self.health}")

    def play(self):
        self.setup()
        self.print_welcome()
        while not self.finished:
            command = input("> ")
            self.process_command(command)

    def process_command(self, command_string):
        words = command_string.split(" ")
        command_word = words[0]

        if command_word not in self.commands:
            print("Commande inconnue. Tapez 'help' pour obtenir la liste des commandes.")
        else:
            command = self.commands[command_word]
            try:
                command.action(self, words, command.number_of_parameters)
            except Exception as e:
                print(f"Erreur : {e}")

    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans la maison hantée !")
        print("Votre mission : explorez chaque pièce et résolvez les énigmes pour découvrir les secrets de la maison.")
        print("Entrez 'help' pour voir les commandes disponibles.")
        print(self.player.current_room.get_long_description())

if __name__ == "__main__":
    Game().play()
