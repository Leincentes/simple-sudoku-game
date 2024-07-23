import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = {}
        self.initialize_board()
        self.create_widgets()

    def initialize_board(self):
        # Initialize an empty 9x9 Sudoku board
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        for row in range(9):
            for col in range(9):
                cell = tk.Entry(frame, width=3, font=('Arial', 18), justify='center')
                cell.grid(row=row, column=col, padx=5, pady=5)
                self.cells[(row, col)] = cell

        self.check_button = tk.Button(self.root, text="Check Solution", command=self.check_solution)
        self.check_button.grid(row=1, column=0, pady=10)
        
        self.solve_button = tk.Button(self.root, text="Solve Puzzle", command=self.solve_puzzle)
        self.solve_button.grid(row=2, column=0, pady=10)

    def check_solution(self):
        if self.read_board():
            if self.is_valid_solution():
                messagebox.showinfo("Success", "Congratulations! You solved the Sudoku puzzle.")
            else:
                messagebox.showerror("Error", "The solution is incorrect. Please try again.")

    def read_board(self):
        for row in range(9):
            for col in range(9):
                try:
                    value = int(self.cells[(row, col)].get()) if self.cells[(row, col)].get() else 0
                    if value < 0 or value > 9:
                        raise ValueError
                    self.board[row][col] = value
                except ValueError:
                    messagebox.showerror("Error", "Invalid input! Please enter numbers between 1 and 9.")
                    return False
        return True

    def is_valid_solution(self):
        return self.is_valid_rows() and self.is_valid_cols() and self.is_valid_boxes()

    def is_valid_rows(self):
        for row in range(9):
            if not self.is_valid_unit(self.board[row]):
                return False
        return True

    def is_valid_cols(self):
        for col in range(9):
            if not self.is_valid_unit([self.board[row][col] for row in range(9)]):
                return False
        return True

    def is_valid_boxes(self):
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        box.append(self.board[row][col])
                if not self.is_valid_unit(box):
                    return False
        return True

    def is_valid_unit(self, unit):
        unit = [i for i in unit if i != 0]
        return len(unit) == len(set(unit))

    def solve_puzzle(self):
        if self.read_board():
            if self.solve():
                self.update_gui_with_solution()
            else:
                messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

    def update_gui_with_solution(self):
        for row in range(9):
            for col in range(9):
                self.cells[(row, col)].delete(0, tk.END)
                self.cells[(row, col)].insert(0, str(self.board[row][col]))

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def find_empty_location(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_safe(self, row, col, num):
        return self.is_safe_in_row(row, num) and self.is_safe_in_col(col, num) and self.is_safe_in_box(row - row % 3, col - col % 3, num)

    def is_safe_in_row(self, row, num):
        return num not in self.board[row]

    def is_safe_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(9)]

    def is_safe_in_box(self, box_start_row, box_start_col, num):
        for i in range(3):
            for j in range(3):
                if self.board[i + box_start_row][j + box_start_col] == num:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
