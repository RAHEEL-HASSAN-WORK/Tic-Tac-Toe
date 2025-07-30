import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="#548687")

# Global variables
current_player = "O"
buttons = []
move_count = 0


# Winning patterns (same as JS)
win_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

# Functions
def check_winner():
    global current_player
    for pattern in win_patterns:
        a, b, c = pattern
        if (buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != ""):
            disable_buttons()
            messagebox.showinfo("Game Over", f"🎉 Winner is {buttons[a]['text']}")
            return True
    return False

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def enable_buttons():
    global move_count
    move_count = 0
    for btn in buttons:
        btn.config(state="normal", text="", bg="#ffffc7")

def button_click(index):
    global current_player, move_count
    if buttons[index]["text"] == "":
        buttons[index].config(text=current_player, fg="#b0413e")
        move_count += 1
        if check_winner():
            return
        if move_count == 9:
            messagebox.showinfo("Game Over", "🤝 It's a draw!")
        current_player = "X" if current_player == "O" else "O"

def new_game():
    global current_player
    current_player = "O"
    enable_buttons()

# Layout
title = tk.Label(root, text="Tic Tac Toe", font=("Arial", 28), bg="#548687", fg="#fff")
title.pack(pady=10)

game_frame = tk.Frame(root, bg="#548687")
game_frame.pack()

for i in range(9):
    btn = tk.Button(game_frame, text="", font=("Arial", 28), width=5, height=2,
                    bg="#ffffc7", activebackground="#f0f0a0",
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

button_frame = tk.Frame(root, bg="#548687")
button_frame.pack(pady=20)

reset_btn = tk.Button(button_frame, text="Reset Game", command=new_game,
                      font=("Arial", 14), bg="#191913", fg="#fff", padx=10, pady=5)
reset_btn.grid(row=0, column=0, padx=10)

new_btn = tk.Button(button_frame, text="New Game", command=new_game,
                    font=("Arial", 14), bg="#191913", fg="#fff", padx=10, pady=5)
new_btn.grid(row=0, column=1, padx=10)

# Run app
root.mainloop()
