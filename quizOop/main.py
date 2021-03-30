from brain import Game

if __name__ == "__main__":
    game = Game()
    while True:
        choice = input(game.generate_question_text())
        game.check_answer(choice)