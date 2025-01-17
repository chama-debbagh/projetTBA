from actions import Actions

# This file contains the Command class.

class Command:
    """
    This class represents a command. A command is composed of a command word, a help string, an action and a number of parameters.

    Attributes:
        command_word (str): The command word.
        help_string (str): The help string.
        action (function): The action to execute when the command is called.
        number_of_parameters (int): The number of parameters expected by the command.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : The constructor.
        __str__(self) : The string representation of the command.

    Examples:

    >>> from actions import go
    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)
    >>> command.command_word
    'go'
    >>> command.help_string
    'Permet de se déplacer dans une direction.'
    >>> type(command.action)
    <class 'function'>
    >>> command.number_of_parameters
    1

    """

    # The constructor.
    """
    Cette classe représente une commande du jeu.

    Attributs :
        command_word (str) : Le mot-clé de la commande.
        help_string (str) : Une description de l'utilisation de la commande.
        action (function) : La fonction à exécuter lorsque la commande est appelée.
        number_of_parameters (int) : Le nombre de paramètres attendus par la commande.
    """

    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self):
        return f"{self.command_word}: {self.help_string}"
