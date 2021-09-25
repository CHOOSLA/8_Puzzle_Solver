from tkinter import *
from PIL import ImageTk,Image
from piece import Piece

win = Tk()
win.title("8 PUZZLE SOLVER")
win.geometry("800x800")
####win.resizable(False, False)

puzzle = LabelFrame(win, width=600, height=600)
puzzle.configure(background='red')
puzzle.grid(column=0, row=0)

piece = []
img = []
count = 0
for i in range(3):
    for j in range(3):
        image = Image.open("img/cloud_gate_"+ str(count) + ".jpg")
        image = image.resize((100,100),Image.ANTIALIAS)
        tmp = ImageTk.PhotoImage(image)

        img.append(tmp)

        Label(puzzle, image=img[count],width=100).grid(column=j, row=i,sticky='w')
        count += 1




print(len(piece))

win.mainloop()
