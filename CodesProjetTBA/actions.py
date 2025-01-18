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

    
    
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        DifferentsO = set (["o","O","OUEST","ouest","Ouest"])
        DifferentsE = set(["e","E","EST","est","Est"])
        DifferentsN = set(["n","N","nord","Nord","NORD"])
        DifferentsU = set(["U","up","monter","haut","UP","Up"])
        DifferentsD = set(["D","down","descendre","en bas","DOWN","Down"])
        DifferentsS = set(["s","S","sud","Sud","SUD"])
       
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1].upper()
        if direction in DifferentsO:
            direction = "O" 
        elif direction in DifferentsE:
            direction = "E"
        elif direction in DifferentsN:
            direction = "N"
        elif direction in DifferentsU:
            direction = "U"
        elif direction in DifferentsD:
            direction ="D"
        elif direction in DifferentsS:
            direction ="S"
        else: 
            print("Cette direction n'est pas valide")
            return False
       # Vérifier si la direction est valide
        if direction not in game.directions:
            print(f"\nDirection '{direction}' non reconnue. Utilisez N, E, S, O, U, D.\n")
            return False
        

        # Move the player in the direction specified by the parameter.
        game.player.move(direction)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
    
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    

    
    def back (game, list_of_words, number_of_parameters):
        if number_of_parameters != 0:
            print("\nLa commande 'back' ne prend pas de paramètres.\n")
            return
        # If the number of parameters is incorrect, print an error message and return False.
        if len(game.player.history) > 1:
            print("\nVous n'avez pas de pièce précédente à laquelle revenir.\n")
            return
        # Retirer la pièce actuelle de l'historique
        game.player.history.pop()

         # Revenir à la pièce précédente
        previous_room_name =game.player.history[-2]
        previous_room = next(room for room in game.rooms if room.name == previous_room_name)
       

        print(f"\nRetour à la pièce précédente : {previous_room.get_long_description()}")

        # Appeler get_history() après chaque retour en arrière
        game.player.get_history()

       
        

    def look(game, list_of_words, number_of_parameters):
        current_room = game.player.current_room
        print(current_room.get_items_description())
        return True
    
    def take(game, list_of_words, number_of_parameters):
        player = game.player
        current_room = player.current_room

        if len(list_of_words) < 2:
            print("Veuillez spécifier l'objet à prendre.")
            return False

        item_names = list_of_words[1:]
        taken_items = []

        for item_name in item_names:
        # Chercher l'objet dans l'inventaire de la pièce
            matching_items = [item for item in current_room.inventory if item.name.lower() == item_name.lower()]

            if not matching_items:
                print(f"{item_name} n'est pas présent dans cette pièce.")
                return False
            # Prendre le premier objet correspondant (si plusieurs)
            item = matching_items[0]
            # Ajouter l'objet à l'inventaire du joueur
            player.add_item_to_inventory(item)
            # Retirer l'objet de l'inventaire de la pièce
            current_room.inventory.remove(item)
            print(f"Vous avez pris {item.name}.")
            return True



#FONCTION DROP

    def drop(game, list_of_words, number_of_parameters):
        player = game.player
        current_room = player.current_room

        if len(list_of_words) < 2:
            print("Veuillez spécifier l'objet à reposer.")
            return False
        
        item_name = list_of_words[1].lower()  

        if item_name in player.inventory:
       # Retirer l'objet de l'inventaire du joueur
            dropped_item = player.inventory.pop(item_name)
                # Ajouter l'objet à la pièce où se trouve le joueur
            current_room.inventory.add(dropped_item)
            print(f"Vous avez reposé {dropped_item.name} dans {current_room.name}.")
            Actions.display_items_in_inventory(player)
            return True

        else:
            print(f"L'objet '{item_name}' n'est pas présent dans votre inventaire.")
            return False

    def display_items_in_inventory(player):
        """
        Display the items in the player's inventory.

        Args:
            player (Player): The player object.

        Returns:
            None
        """
        if not player.inventory:
            print("\nVotre inventaire est vide.\n")
        else:
            print("\nObjets dans votre inventaire:")
            for item in player.inventory.values():
                print(f"\t- {item.name}")
            print()