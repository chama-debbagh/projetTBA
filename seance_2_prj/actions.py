from item import Item
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
from item import Item

class Actions:

    def go(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1].upper()
        if direction not in game.directions:
            print(f"\nDirection '{direction}' non reconnue. Utilisez N, E, S, O, U, D.\n")
            return False

        player.move(direction)
        return True

   
    
    def solve(game, list_of_words, number_of_parameters):
        player = game.player
        current_room = player.current_room

        if current_room.puzzle_solved:
        print("\nVous avez déjà résolu l'énigme ici.")
        print(current_room.get_exit_string())  # Affiche les choix disponibles
        return True

        attempt = input(f"\n{current_room.puzzle}\nVotre réponse : ")
        current_room.solve_puzzle(attempt)

        if current_room.puzzle_solved:
        print(current_room.get_exit_string())  # Affiche les choix disponibles
        return True


    def inspect(game, list_of_words, number_of_parameters):
        """
        Inspecter la pièce pour trouver des indices ou des dangers.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'inspect' ne prend pas de paramètre.\n")
            return False

        print("\nVous inspectez la pièce...")
        if "piège" in game.player.current_room.description.lower():
            print("Oh non ! Vous avez déclenché un piège !")
            game.reduce_health(20)
        else:
            print("Vous trouvez un indice utile.")
        return True

    def quit(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        print(f"\nMerci {player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\nVoici les commandes disponibles :")
        for command in game.commands.values():
            print(f"  - {command}")
        print()
        return True
