class Riddle:
    """
    Classe représentant une énigme avec sa question et sa réponse.
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer.lower()  # Convertit la réponse en minuscules

    def check_answer(self, player_answer):
        """Vérifie si la réponse du joueur est correcte."""
        return player_answer.lower() == self.answer