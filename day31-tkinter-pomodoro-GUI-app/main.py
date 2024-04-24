from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # Update: timer_text to "00:00", title_label to "Timer" and reset the check mark
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    check_marks.config(text="")
    global repetitions
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global repetitions
    repetitions += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th
    # count_down(work_sec)
    # if it's 8th
    # count_down(long_break_sec)
    # If it's 2nd/4th/6th
    # count_down(short_break_sec)
    if repetitions % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW)
    elif repetitions % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        # Every work session we need a check mark, by every two repetitions means the work is completed.
        marks = ""
        for _ in range(math.floor(repetitions / 2)):
            marks += "✔"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Start Button
start_button = Button(text="Start", width=2, command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", width=2, command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmark ✔
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
