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

class Actions:

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'go' nécessite une direction.")
            return False

        direction = list_of_words[1].upper()
        if direction in game.directions:
            game.player.move(direction)
            return True
        else:
            print("\nDirection invalide. Utilisez N, E, S, O.")
            return False

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'quit' ne prend pas de paramètres.")
            return False

        print(f"\nMerci d'avoir joué, {game.player.name} ! Au revoir.")
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'help' ne prend pas de paramètres.")
            return False

        print("\nVoici les commandes disponibles :")
        for command in game.commands.values():
            print(f"  - {command.command_word}: {command.help_string}")
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'look' ne prend pas de paramètres.")
            return False

        print(game.player.current_room.get_long_description())
        return True
