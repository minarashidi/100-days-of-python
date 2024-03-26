from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []
for question in question_data:
    question_list.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_list)

while quiz_brain.has_questions():
    user_answer = quiz_brain.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.current_question_number}")
