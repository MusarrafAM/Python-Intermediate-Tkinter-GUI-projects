from tkinter import *
import math


# pomodoro = tomato in italian
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    label_timer.config(text="Timer")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label_checkbox.config(text="")
    global reps
    reps = 0
    button_start.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    button_start.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# ########### Very important but simple try to understand just like recursion. #######

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # This is how we change the canvas text.
    # label_timer.config(text="change") ## This is how we change a text in label or button. in canvas its different.
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # here 1000 milliseconds
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        label_checkbox.config(text=marks)
        # to bring the app in-front of all other windows.
        raise_above_all()

def raise_above_all():
    window.attributes("-topmost", 1)
    window.attributes("-topmost", 0)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)
window.lift()   # to bring the window front mechanism.

canvas = Canvas(width=200, height=224, bg=GREEN,
                highlightthickness=0)  # using this highlightthickness to get rid of the white square boarder.
tomato_image = PhotoImage(file="tomato.png")  # canvas only accept PhotoImage files. so first need to change
canvas.create_image(100, 112, image=tomato_image)  # first x and y-axis then the image.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label 1
label_timer = Label(text="Timer", font=(FONT_NAME, 40), fg=RED, bg=GREEN)
label_timer.grid(column=1, row=0)

# Start button 1
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

# reset button 2
reset_start = Button(text="Reset", command=reset_timer)
reset_start.grid(column=2, row=2)

# checkbox label 2
label_checkbox = Label(font=(FONT_NAME, 20), fg=RED, bg=GREEN)
label_checkbox.grid(column=1, row=3)

window.mainloop()

#  ############################ Important    #################
# import time
# x = 10
# while x != 0:
#     print(x)
#     time.sleep(1)
#     x -= 1












