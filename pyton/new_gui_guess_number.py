import numpy as np
import tkinter as tk
from tkinter import messagebox

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.current_arr_index = 0
        self.matrix_size = (6, 5)  # Default matrix size
        self.sum_of_first_elements = 0

        self.create_matrices()

        # Bind the window resize event
        self.root.bind("<Configure>", self.on_window_resize)

    def create_matrices(self):
        # Define the matrices
        self.arr1 = np.random.randint(1, 61, size=self.matrix_size)
        self.arr2 = np.random.randint(1, 61, size=self.matrix_size)
        self.arr3 = np.random.randint(1, 61, size=self.matrix_size)
        self.arr4 = np.random.randint(1, 61, size=self.matrix_size)
        self.arr5 = np.random.randint(1, 61, size=self.matrix_size)
        self.arr6 = np.random.randint(1, 61, size=self.matrix_size)

        self.show_matrix()

    def show_matrix(self):
        self.matrix_label = tk.Label(self.root, text=str(self.get_current_arr()), relief="groove", padx=10, pady=10)
        self.matrix_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.yes_button = tk.Button(self.root, text="Yes", command=self.yes_action)
        self.yes_button.grid(row=1, column=0)

        self.no_button = tk.Button(self.root, text="No", command=self.no_action)
        self.no_button.grid(row=1, column=2)

    def get_current_arr(self):
        if self.current_arr_index == 0:
            return self.arr1
        elif self.current_arr_index == 1:
            return self.arr2
        elif self.current_arr_index == 2:
            return self.arr3
        elif self.current_arr_index == 3:
            return self.arr4
        elif self.current_arr_index == 4:
            return self.arr5
        elif self.current_arr_index == 5:
            return self.arr6

    def show_next_matrix(self):
        if self.current_arr_index == 5:
            messagebox.showinfo("Game Over", f"Sum of first elements of matrices where 'Yes' was selected: {self.sum_of_first_elements}")
            self.root.destroy()
        else:
            self.current_arr_index += 1
            self.matrix_label.config(text=str(self.get_current_arr()))

    def yes_action(self):
        self.sum_of_first_elements += int(self.get_current_arr()[0, 0])
        self.show_next_matrix()

    def no_action(self):
        self.show_next_matrix()

    def on_window_resize(self, event):
        # Update matrix size when window is resized
        new_rows = max(1, int(self.root.winfo_height() / 30))  # Assuming average row height of 30 pixels
        new_columns = max(1, int(self.root.winfo_width() / 60))  # Assuming average column width of 60 pixels

        self.matrix_size = (new_rows, new_columns)
        self.create_matrices()

root = tk.Tk()
app = NumberGuessingApp(root)
root.mainloop()
