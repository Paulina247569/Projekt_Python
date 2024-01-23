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
