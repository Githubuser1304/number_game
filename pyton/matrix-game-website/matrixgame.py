


import numpy as np
import tkinter as tk
from tkinter import messagebox

def move_left(event=None):
    global count
    global arr
    x, y = np.where(arr == 0)
    if y > 0:
        arr[x, y], arr[x, y - 1] = arr[x, y - 1], arr[x, y]  # swapping
        update_board()
        count -= 1
        lbl_steps_left.config(text="Steps left: " + str(count))
    else:
        messagebox.showinfo("Error", "Cannot move left")

def move_right(event=None):
    global count
    global arr
    x, y = np.where(arr == 0)
    if y < 3:
        arr[x, y], arr[x, y + 1] = arr[x, y + 1], arr[x, y]  # swapping
        update_board()
        count -= 1
        lbl_steps_left.config(text="Steps left: " + str(count))
    else:
        messagebox.showinfo("Error", "Cannot move right")

def move_up(event=None):
    global count
    global arr
    x, y = np.where(arr == 0)
    if x > 0:
        arr[x, y], arr[x - 1, y] = arr[x - 1, y], arr[x, y]  # swapping
        update_board()
        count -= 1
        lbl_steps_left.config(text="Steps left: " + str(count))
    else:
        messagebox.showinfo("Error", "Cannot move up")

def move_down(event=None):
    global count
    global arr
    x, y = np.where(arr == 0)
    if x < 3:
        arr[x, y], arr[x + 1, y] = arr[x + 1, y], arr[x, y]  # swapping
        update_board()
        count -= 1
        lbl_steps_left.config(text="Steps left: " + str(count))
    else:
        messagebox.showinfo("Error", "Cannot move down")

def update_board():
    for i in range(4):
        for j in range(4):
            btn_board[i][j].config(text=str(arr[i, j]))

def check_win():
    global arr
    global arr2
    if np.array_equal(arr, arr2):
        messagebox.showinfo("Congratulations", "You won!!")

def quit_game():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Matrix Game")
root.configure(background="grey")  # Set main window background color

# Initialize game variables
count = 1000
unique_numbers = np.random.permutation(16)
arr = unique_numbers.reshape((4, 4))
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

# Create the board buttons
btn_board = []
for i in range(4):
    row = []
    for j in range(4):
        btn = tk.Button(root, text=str(arr[i, j]), width=5, height=2, command=lambda i=i, j=j: None, bg="white", fg="black")
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    btn_board.append(row)
btn_left = tk.Button(root, text="Left", width=10, command=move_left, bg="grey", fg="white")
btn_left.grid(row=4, column=0, padx=5, pady=5)
btn_right = tk.Button(root, text="Right", width=10, command=move_right, bg="grey", fg="white")
btn_right.grid(row=4, column=1, padx=5, pady=5)
btn_up = tk.Button(root, text="Up", width=10, command=move_up, bg="grey", fg="white")
btn_up.grid(row=4, column=2, padx=5, pady=5)
btn_down = tk.Button(root, text="Down", width=10, command=move_down, bg="grey", fg="white")
btn_down.grid(row=4, column=3, padx=5, pady=5)

# Display steps left
lbl_steps_left = tk.Label(root, text="Steps left: " + str(count))
lbl_steps_left.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Check for win condition
check_win()

# Bind arrow keys to corresponding functions
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

# Quit button
btn_quit = tk.Button(root, text="Quit", command=quit_game)
btn_quit.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()