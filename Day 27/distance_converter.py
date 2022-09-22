import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(300, 300)


def convert():
    miles = float(entry.get())
    kmLabel.config(text=miles * 1.609)


milesLabel = tkinter.Label(text="Miles")
kmLabel = tkinter.Label(text="Km")
equalLabel = tkinter.Label(text="is equal to")

entry = tkinter.Entry()

calcButton = tkinter.Button(text="Calculate", command=convert)

milesLabel.pack()
kmLabel.pack()
equalLabel.pack()
entry.pack()
calcButton.pack()

window.mainloop()
