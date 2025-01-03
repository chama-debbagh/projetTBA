# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history=[] #initialisation de l historique avec une liste videee
    

    def get_history(self):
        """ retourner une representation des rooms qu'on a visiter. mais n'inclue pas la room actuelle
        """
        if not self.history:  #s'il y a rien dans l'historique
           return ""
        history_string="\nVous avez deja visiter les pieces suivantes:"
        for room in self.history :
            history_string+= f"\n    -{room.description} "
        return history_string
    
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        self.history.append(self.current_room) #ajout de la position precedente du joueur a l historique
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

    