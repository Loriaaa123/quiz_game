from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_quest: QuizBrain):
        self.quiz = quiz_quest

        self.window = Tk()
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.window.title("Quizzzing")

        self.sc_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.sc_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quest_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question?",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.next_quest()

        self.window.mainloop()

    def next_quest(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            quest_n = self.quiz.next_question()
            self.sc_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quest_text, text=quest_n)
        else:
            self.canvas.itemconfig(self.quest_text, text="End of The Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def give_feedback(self, right):
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(250, self.next_quest)

