from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
TICK = "✓"
reps = 0
timer = None


def resetTimer():
    window.after_cancel(timer)
    timerLabel.config(text="Timer")
    tickLabel.config(text="")
    canvas.itemconfig(timerCanvas, text="00:00")
    global reps
    reps = 0


def startTimer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countDown(LONG_BREAK_MIN * 60)
        timerLabel.config(fg=GREEN, text="Big pause")
    elif reps % 2 == 0:
        countDown(SHORT_BREAK_MIN * 60)
        timerLabel.config(fg=GREEN, text="Small pause")
    else:
        countDown(WORK_MIN * 60)
        timerLabel.config(fg=RED, text="Work")


def countDown(count):
    count_min = count // 60
    count_seconds = count % 60
    canvas.itemconfig(
        timerCanvas, text=f"{'0' * (2- len(str(count_min))) + str(count_min)}:{'0' * (2- len(str(count_seconds))) + str(count_seconds)}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        startTimer()
        global reps
        tickLabel.config(text=f"{TICK * (reps // 2)}")


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=233, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="Day 28/tomato.png")
canvas.create_image(100, 112, image=tomato)
timerCanvas = canvas.create_text(102, 130, text="00:00", fill="white",
                                 font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timerLabel = Label(text="Timer", font=(
    FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timerLabel.grid(column=1, row=0)

startButton = Button(text="Start", command=startTimer)
startButton.grid(column=0, row=2)

resetButton = Button(text="Reset", command=resetTimer)
resetButton.grid(column=2, row=2)

tickLabel = Label(text="", font=(
    FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
tickLabel.grid(column=1, row=3)


window.mainloop()
