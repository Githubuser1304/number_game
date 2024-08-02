import numpy as np
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.config(bg="#ccd5ae")
root.geometry("500x500")

# Define the matrices
arr1 = np.array([[1, 3, 5, 7, 9], [11, 13, 15, 17, 19], [21, 23, 25, 27, 29], [31, 33, 35, 37, 39], [41, 43, 45, 47, 49], [51, 53, 55, 57, 59]])
arr2 = np.array([[2, 3, 6, 7, 10], [11, 14, 15, 18, 19], [22, 23, 26, 27, 30], [31, 34, 35, 38, 39], [42, 43, 46, 47, 50], [51, 54, 55, 58, 59]])
arr3 = np.array([[4, 5, 6, 7, 11], [12, 13, 14, 15, 20], [21, 22, 23, 28, 29], [30, 31, 36, 37, 38], [39, 44, 45, 46, 47], [52, 53, 55, 60, ' ']])
arr4 = np.array([[8, 9, 10, 11, 12], [13, 14, 15, 24, 25], [26, 27, 28, 29, 30], [31, 40, 41, 42, 43], [44, 45, 46, 47, 56], [57, 58, 59, 60, ' ']])
arr5 = np.array([[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30], [31, 48, 49, 50, 51], [52, 53, 54, 55, 56], [57, 58, 59, 60, ' ']])
arr6 = np.array([[32, 33, 34, 35, 36], [37, 38, 39, 40, 41], [42, 43, 44, 45, 46], [47, 48, 49, 50, 51], [52, 53, 54, 55, 56], [57, 58, 59, 60, ' ']])

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.current_arr_index = 0
        self.current_arr = arr1
        self.sum_of_first_elements = 0

        self.show_matrix()

    def show_matrix(self):
        # self.label = tk.Label(self.root,text="        ")
        self.matrix_label = tk.Label(self.root, text=str(self.current_arr), relief="groove", padx=20, pady=20,bg = "grey", fg="black", bd=5)

        # self.matrix_label.grid(row=0, column=0, columnspan=3)
        self.matrix_label.place(relx=0.5, rely=0.5, anchor="center")

        self.yes_button = tk.Button(self.root, text="Yes", command=self.yes_action,bg="green",padx=10)
        # self.yes_button.grid(row=1, column=0)
        self.yes_button.place(relx=0.4, rely=0.7, anchor="center")

        self.no_button = tk.Button(self.root, text="No", command=self.no_action,bg="red",padx = 10)
        self.no_button.place(relx=0.6, rely=0.7, anchor="center")

    def show_next_matrix(self):
        if self.current_arr_index == 5:
            messagebox.showinfo("Game Over", f"Your guessed number is : {self.sum_of_first_elements}")
            self.root.destroy()
        else:
            self.current_arr_index += 1
            if self.current_arr_index == 1:
                self.current_arr = arr2
            elif self.current_arr_index == 2:
                self.current_arr = arr3
            elif self.current_arr_index == 3:
                self.current_arr = arr4
            elif self.current_arr_index == 4:
                self.current_arr = arr5
            elif self.current_arr_index == 5:
                self.current_arr = arr6
            self.matrix_label.config(text=str(self.current_arr))

    def yes_action(self):
        self.sum_of_first_elements += int(self.current_arr[0, 0])
        self.show_next_matrix()

    def no_action(self):
        self.show_next_matrix()
app = NumberGuessingApp(root)

root.mainloop()
