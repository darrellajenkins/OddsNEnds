import pandas

import random

import tkinter

data = pandas.read_csv("quotes1revised.csv")
newdict = {row.Quote: row.Author for (index, row) in data.iterrows()}
random_quotes = random.sample(list(newdict.items()), min(1602, len(newdict.items())))
random_quote = [random.choice(random_quotes) for item in random_quotes]

win = tkinter.Tk()
win.title("100 Days of Python - YOU Can Do It!")
win.config(padx=40, pady=40, bg="white")

count = 11

def check():
    global count
    count -= 1
    label_1.config(text=f"{random.choice(random_quote)}", wraplength=500)
    if count <= 1:
        tomorrow()

def tomorrow():
    label_1.config(text="Come back tomorrow for more inspiration.  Now go code!", fg="blue", bg="#219C90", font=("Aharoni", 16, "normal"))
    label_3.destroy()
    button_2["state"] = "disabled"
    
label_2 = tkinter.Label(text="Today is a great day to continue from where you left off.\nNever give up. You will succeed!", fg="black", bg="#FFB000", font=("Vivaldi", 16, "bold", "normal"))
label_2.grid(column=2, row=1)
label_2.config(padx=39)

label_1 = tkinter.Label(text="Imagine what you can achieve today ~ DJ", fg="black", bg="#F2BE22", font=("Forte", 14, "normal"))
label_1.grid(column=2, row=3)
label_1.config(padx=53, pady=8)

label_3 = tkinter.Label(text="Click for more inspiration", fg="#862B0D", bg="white", font=("Forte", 12, "bold"))
label_3.grid(column=2, row=99)

button_2 = tkinter.Button(text="MORE", fg="black", bg="#116D6E", font=("Arial", 12, "bold"), height=1, width=4, command=check)
button_2.grid(column=2, row=5)
button_2.config(padx=5, pady=5)

iguazu = tkinter.PhotoImage(file='iguazu.png')
kirkjufell = tkinter.PhotoImage(file='kirkjufell.png')

canvas = tkinter.Canvas(width=500, height=400, highlightthickness=5, highlightbackground="white")
canvas.create_image((175, 200), image=iguazu)
canvas.grid(column=2, row=2)

def nextimage():
    canvas = tkinter.Canvas(width=500, height=400, highlightthickness=5, highlightbackground="white")
    canvas.create_image((175, 200), image=kirkjufell)
    canvas.grid(column=2, row=2)

canvas.after(8000, nextimage)

win.mainloop()

