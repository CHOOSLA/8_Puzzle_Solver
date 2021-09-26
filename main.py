import random
import threading
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

import astar
from astar import *


def updatePuzzle(board):
    for i in range(9):
        piece[i].grid(column=board[i] % 3, row=int(board[i] / 3))
    win.update()


def randomize():
    random.shuffle(puzzle)
    updatePuzzle(puzzle)


def search():
    searchButton['state'] = DISABLED
    loopChosen['state'] = DISABLED
    randomizeButton['state'] = DISABLED
    # open 리스트는 우선순위 큐로 생성한다.
    open_queue = queue.PriorityQueue()

    open_queue.put(State(puzzle, goal))

    closed_queue = []

    count = 0;
    while not open_queue.empty() and (count < int(loopChosen.get()) or int(loopChosen.get()) == -1):
        #  디버깅을 위한 코드
        #  print("START OF OPENQ")
        #  for elem in open_queue.queue:
        #        print(elem)
        #  print("END OF OPENQ")

        current = open_queue.get()
        count += 1
        print(count)

        updatePuzzle(current.board)
        if current.board == goal:
            updatePuzzle(current.board)
            print(current)
            print("탐색 성공")
            print("open queue 길이=", open_queue.qsize())
            print("closed queue 길이=", len(closed_queue))
            updatePuzzle()
            break
        moves = current.moves + 1
        for state in current.expand(moves):
            if state not in closed_queue and state not in open_queue.queue:
                open_queue.put(state)
        closed_queue.append(current)
    else:
        print('탐색 실패')

    randomizeButton['state'] = NORMAL
    searchButton['state'] = NORMAL
    loopChosen['state'] = NORMAL


def threadSearch():
    t = threading.Thread(target=search)
    t.start()


# 초기 상태
puzzle = [0, 1, 2,
          3, 4, 5,
          6, 7, 8]

# 목표 상태
goal = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]

win = Tk()
win.title("8 PUZZLE SOLVER")
win.geometry("400x800")
####win.resizable(False, False)

leftPanel = LabelFrame(win, width=400)
leftPanel.pack(fill='y', side='left')


puzzlePanel = LabelFrame(leftPanel, width=600, height=600)
puzzlePanel.configure(background='red')
puzzlePanel.grid(column=0, row=0, padx=50, pady=50)

piece = []
img = []
count = 0
for i in range(3):
    for j in range(3):
        image = Image.open("img/cloud_gate_" + str(count) + ".jpg")
        image = image.resize((100, 100), Image.ANTIALIAS)
        tmp = ImageTk.PhotoImage(image)

        img.append(tmp)

        lbl = Label(puzzlePanel, background='red', text=count, image=img[count], width=100)
        lbl.grid(column=j, row=i)
        piece.append(lbl)
        count += 1

piece[8].configure(background='blue')

buttonPanel = LabelFrame(leftPanel)
buttonPanel.configure(background='white')
buttonPanel.grid(column=0, row=2, padx=50, pady=50)

loop = 10000

loopChosen = ttk.Combobox(buttonPanel, width=12, textvariable=loop)
loopChosen.grid(column=0, row=0, padx=10, pady=10)
loopChosen['values'] = (-1, 10000, 20000, 50000, 100000)
loopChosen.current(1)

randomizeButton = Button(buttonPanel, text="Randomize", width=30, height=5, command=randomize)
randomizeButton.grid(column=0, row=1, padx=10, pady=10)
searchButton = Button(buttonPanel, text="Search", width=30, height=5, command=threadSearch)
searchButton.grid(column=0, row=2, padx=10, pady=10)

# 목표 상태
goal = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]

open_queue = queue.PriorityQueue()
closed_queue = []
moves = 0

win.mainloop()
