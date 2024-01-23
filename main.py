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
    class Food:
        def __init__(self, canvas):
            self.canvas = canvas
            x = random.randint(0, (game_width // space_size) - 1) * space_size
            y = random.randint(0, (game_height // space_size) - 1) * space_size
            self.coordinates = [x, y]
            self.canvas.create_oval(x, y, x + space_size, y + space_size, fill=food_color, tag="food")

    def next_turn(snake, food):
        x, y = snake.coordinates[0]

        if direction == "up":
            y -= space_size
        elif direction == "down":
            y += space_size
        elif direction == "left":
            x -= space_size
        elif direction == "right":
            x += space_size
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            score += 1
            label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food(canvas)
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            game_over()
        else:
            window.after(speed, next_turn, snake, food)
