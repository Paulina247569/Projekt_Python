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

    def change_direction(new_direction):
        global direction
        if new_direction == "left" and direction != "right":
            direction = new_direction
        elif new_direction == "right" and direction != "left":
            direction = new_direction
        elif new_direction == "up" and direction != "down":
            direction = new_direction
        elif new_direction == "down" and direction != "up":
            direction = new_direction

    def check_collisions(snake):
        x, y = snake.coordinates[0]

        if x < 0 or x >= game_width:
            return True
        elif y < 0 or y >= game_height:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                print("GAME OVER")
                return True

        return False

    def game_over():
        canvas.delete(tk.ALL)
        canvas.create_text(game_width / 2, game_height / 2, font=("consolas", 70), text="GAME OVER", fill="red",
                           tag="gameover")
        canvas.create_text(game_width / 2, game_height / 1.5 + 50, font=("consolas", 40),
                               text="Player: {}\nScore: {}".format(username, score), fill="red", tag="gameover")

    def set_window_geometry(window):
        window_width = int(window.winfo_width())
        window_height = int(window.winfo_height())
        screen_width = int(window.winfo_screenwidth())
        screen_height = int(window.winfo_screenheight())

        x = int(screen_width / 2) - int(window_width / 2)
        y = int(screen_height / 2) - int(window_height / 2)
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def show_high_scores():
        high_scores_window = tk.Toplevel(window)
        high_scores_window.title("High Scores")
        high_scores_window.geometry("300x200")

        scores_label = tk.Label(high_scores_window, text="High Scores", font=('consolas', 18, 'bold'))
        scores_label.pack()

        
        high_scores = ["Player1: 10", "Player2: 8", "Player3: 5"]

        for score in high_scores:
            score_label = tk.Label(high_scores_window, text=score, font=('consolas', 14))
            score_label.pack()

    window = tk.Tk()
    window.title("Snake game")
    window.resizable(False, False)

    label = tk.Label(window, text="Score: {}".format(score), font=('consolas', 40))
    label.pack()

    canvas = tk.Canvas(window, bg=background_color, height=game_height, width=game_width)
    canvas.pack()

    window.update()

    set_window_geometry(window)

    window.bind("<KeyPress-Left>", lambda event: change_direction("left"))
    window.bind("<KeyPress-Right>", lambda event: change_direction("right"))
    window.bind("<KeyPress-Up>", lambda event: change_direction("up"))
    window.bind("<KeyPress-Down>", lambda event: change_direction("down"))

    snake = Snake()
    food = Food(canvas)

    next_turn(snake, food)

    menu = tk.Menu(window)
    window.config(menu=menu)
    high_scores_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Menu", menu=high_scores_menu)
    high_scores_menu.add_command(label="High Score", command=show_high_scores)

    window.mainloop()

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
