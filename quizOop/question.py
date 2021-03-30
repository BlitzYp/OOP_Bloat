class Question:
    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer
    
    def check_if_correct(self, answer: str) -> bool:
        """Checks if the user answer matches to the actual answer"""
        if answer == self.answer:
            return True
        return False

    


