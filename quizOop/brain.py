from question import Question
from random import choice
from data import question_data

class Game:
    DATA = [Question(i.get("text"), i.get("answer")) for i in question_data]
    def __init__(self):
        self.game_count: int = 0
        self.player_score: int = 0
        self.chosen: Question = {}
    
    def generate_question(self) -> Question:
        self.chosen = choice(self.DATA)
        return self.chosen
    
    def check_answer(self, answer: str) -> bool:
        if self.chosen.check_if_correct(answer):
            self.player_score += 1
            print("You got it right!")
        else: print("You got it wrong!")
        print("The correct answer was: {}.".format(self.chosen.answer))
        print(f"Your current score: {self.player_score}/{self.game_count}")

    def generate_question_text(self) -> str:
        answer = self.generate_question()
        self.game_count += 1
        return "Q.{}: {} (True/False): ".format(self.game_count, answer.text)