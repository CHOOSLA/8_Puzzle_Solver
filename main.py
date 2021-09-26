import random
from tkinter import *
from PIL import ImageTk, Image
from piece import Piece


def updatePuzzle():
    count = 0
    for i in range(3):
        for j in range(3):
            piece[count].grid(column=j, row=i)
            count += 1
    win.update()


def randomize():
    random.shuffle(piece)
    updatePuzzle()


win = Tk()
win.title("8 PUZZLE SOLVER")
win.geometry("1200x800")
####win.resizable(False, False)

leftPanel = LabelFrame(win, width=400)
leftPanel.configure(background='black')
leftPanel.pack(fill='y', side='left')

rightPanel = LabelFrame(win, width=400)
rightPanel.configure(background='black')
rightPanel.pack(fill='both', expand=1, side='right')

puzzle = LabelFrame(leftPanel, width=600, height=600)
puzzle.configure(background='red')
puzzle.grid(column=0, row=0, padx=50, pady=50)

piece = []
img = []
count = 0
for i in range(3):
    for j in range(3):
        image = Image.open("img/cloud_gate_" + str(count) + ".jpg")
        image = image.resize((100, 100), Image.ANTIALIAS)
        tmp = ImageTk.PhotoImage(image)

        img.append(tmp)

        lbl = Label(puzzle, background='red', image=img[count], width=100)
        lbl.grid(column=j, row=i)
        piece.append(lbl)
        count += 1

piece[8].configure(background='blue')

buttonPanel = LabelFrame(leftPanel)
buttonPanel.configure(background='white')
buttonPanel.grid(column=0, row=2, padx=50, pady=50)

Button(buttonPanel, text="Randomize", width=30, height=5, command=randomize).grid(column=0, row=0, padx=10, pady=10)
Button(buttonPanel, text="Search", width=30, height=5).grid(column=0, row=5, padx=10, pady=10)

win.mainloop()
