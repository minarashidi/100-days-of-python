from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BG_COLOR = "#FFFFFF"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score:", font=(FONT_NAME, 20, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some questions", fill=THEME_COLOR,
                                                     font=(FONT_NAME, 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()  # never ending while loop, it's constantly checking if it needs to update something in the graphical user interface

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            next_question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have answered all questions!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)

    def check_false(self):
        is_true = self.quiz.check_answer("False")
        self.give_feedback(is_true)

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
