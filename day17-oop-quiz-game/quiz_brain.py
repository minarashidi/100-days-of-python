class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions[self.current_question_number]
        self.current_question_number += 1
        # Q1: A slug's blood is green.(True/False)
        user_answer = input(f"Q{self.current_question_number} - {current_question.text} (True/False)?:")
        self.check_answer(user_answer, current_question.answer)

    def has_questions(self):
        return self.current_question_number < len(self.questions)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer == user_answer:
            self.score += 1
            print("That's correct!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"The current score was: {self.score}/{self.current_question_number}")
