import tkinter as tk
import random

score = 0
direction = "down"

def open_game(username):
    window1.destroy()

    game_width = 700
    game_height = 700
    speed = 200
    space_size = 50
    body_parts = 3

    snake_color = 'blue'
    food_color = 'red'
    background_color = 'light green'

    class Snake:
        def __init__(self):
            self.body_size = body_parts
            self.coordinates = []
            self.squares = []
            self.direction = "down"

            for _ in range(0, body_parts):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag="snake")
                self.squares.append(square)























def start_game():
    username = entry.get()
    if username:
        open_game(username)


window1 = tk.Tk()
window1.title("Game")
window1.geometry("600x600")

frame = tk.Frame(window1)

lbTitle = tk.Label(frame, text="Snake", font='Helvetica 18 bold')
lbTitle.pack()

entry = tk.Entry(frame, font='Helvetica 14')
entry.pack()

btnGame = tk.Button(frame, text="Start", font='Helvetica 20 bold', command=start_game)
btnGame.config(bg="#c7de9b")
btnGame.pack()

btnClose = tk.Button(frame, text="Close", font='Helvetica 20 bold', command=window1.destroy)
btnClose.config(bg="#dea59b")
btnClose.pack()

frame.pack(anchor='center', pady=100)

window1.mainloop()