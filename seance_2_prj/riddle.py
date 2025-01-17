class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer.lower()

    def check_answer(self, player_answer):
        return player_answer.lower() == self.answer