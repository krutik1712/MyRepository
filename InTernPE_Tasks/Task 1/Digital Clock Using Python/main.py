from tkinter import Tk, Label
import time

root = Tk()
root.title("Digital Clock")

def present_time():
    display_time = time.strftime("%H:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)

digi_clock = Label(root, font=("arial", 85),bg="white",fg="black")
digi_clock.pack()

present_time()
root.mainloop()
