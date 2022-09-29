from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR,
                                 fg="white")
        self.score_label.grid(row=0, column=1)
        self.question_canvas = Canvas(height=250, width=300, bg="white",
                                      highlightthickness=0)
        self.question = self.question_canvas.create_text(150, 125,
                                                         text="Question", font=(
                "Arial", 15, "italic"), fill=THEME_COLOR, width=270)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR,
                                  highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR,
                                   highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            self.question_canvas.itemconfig(self.question,
                                        text=self.quiz_brain.next_question())
        else:
            self.question_canvas.itemconfig(self.question, text="There are no more questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right:bool):
        if is_right:
            self.question_canvas.config(bg="green")
            self.score += 1
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
