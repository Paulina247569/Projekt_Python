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