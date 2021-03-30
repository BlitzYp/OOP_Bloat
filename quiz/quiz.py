#from data import question_data
from random import choice
from typing import List
import requests

question_data = requests.get("https://opentdb.com/api.php?amount=10&category=18").json()["results"]

def get_question(chosen: List[dict]) -> dict:
    res = choice(list(filter(lambda x: not x in chosen, question_data)))
    chosen.append(res)
    return res

if __name__ == "__main__":
    counter = 1
    chosen = []
    score = 0
    while True:
        question = get_question(chosen)
        user_choice = input("Q.{}: {}: ".format(counter, question["question"]))
        if user_choice == question["correct_answer"]: 
            print("You got it right!")
            score += 1
        else: print("You got it wrong!")
        print("The correct answer was: {}".format(question.get("correct_answer")))
        print(f"Your current score is: {score}/{counter}")
        counter += 1