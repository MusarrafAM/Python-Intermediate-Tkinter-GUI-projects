from tkinter import *
import pandas
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words-to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    french = current_card["French"]
    canvas.itemconfig(canvas_image, image=img_front)
    canvas.itemconfig(text_title, text="French", fill="black")
    canvas.itemconfig(text_word, text=french, fill="black")
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words-to_learn.csv", index=False)
    next_card()


def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=img_back)




window = Tk()
window.title("Flashy")
window.minsize(width=1000, height=750)
window.config(bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

img_back = PhotoImage(file="images/card_back.png")
img_front = PhotoImage(file="images/card_front.png")
img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")


canvas_image = canvas.create_image(400, 263, image=img_front)   # we need to put the half size of canvas here(x,y).
                                                               # to center the pic.

text_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

text_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


canvas.place(x=100, y=50)


# button
right_button = Button(image=img_right, highlightthickness=0, command=is_known)
right_button.place(x=650, y=590)


wrong_button = Button(image=img_wrong, highlightthickness=0, command=next_card)
wrong_button.place(x=250, y=590)


next_card()

window.mainloop()
