from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # this quiz_brain variable must be a QuizBrain data type. watch video 307 if dont get it.
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        # self.window.minsize(width=400, height=600)  no need this for grid method.

        # score label
        self.score_label_total = Label(text=f"Question number: {self.quiz.question_number}", bg=THEME_COLOR, fg="white",
                                 font=("arial", 12, "bold"))
        self.score_label_total.grid(row=0, column=0)


        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        # crete canvas
        self.canvas = Canvas(width=300, height=250,bg="white")
        # put text inside canvas
        self.question_text = self.canvas.create_text(150, 125,width=280 , text="Some questions text",
                                                     font=("arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        # load images
        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        # create buttons
        self.correct_button = Button(image=correct_image, highlightthickness=0, bd=0, command=self.press_correct_button)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=self.press_wrong_button)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.wrong_button.config(state="normal")
        self.correct_button.config(state="normal")
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.score_label_total.config(text=f"Question number: {self.quiz.question_number}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz. ")
            self.wrong_button.config(state="disabled")
            self.correct_button.config(state="disabled")

    def press_correct_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_wrong_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.wrong_button.config(state="disabled")
        self.correct_button.config(state="disabled")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

