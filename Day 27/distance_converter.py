from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)


def convert():
    miles = float(entry.get())
    resultLabel.config(text=miles * 1.609)


milesLabel = Label(text="Miles")
kmLabel = Label(text="Km")
equalLabel = Label(text="is equal to")
resultLabel = Label(text="")

entry = Entry()
entry.config(width=10)

calcButton = Button(text="Calculate", command=convert)

entry.grid(column=1, row=0, padx=10)
milesLabel.grid(column=2, row=0)
equalLabel.grid(column=0, row=1)
resultLabel.grid(column=1, row=1)
kmLabel.grid(column=2, row=1)
calcButton.grid(column=1, row=2)

window.mainloop()
