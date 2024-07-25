import tkinter as tk
from tkinter import messagebox, scrolledtext
from sudoku import Sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.root.geometry("515x540") 
        self.root.resizable(False, False)
        
        self.sudoku = Sudoku()
        self.cells = {}
        self.difficulty = 'easy'
        self.initialize_board()
        self.create_widgets()

    def initialize_board(self):
        self.sudoku.initialize_board()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        self.create_grid(frame)
        self.create_buttons()

    def create_grid(self, frame):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(frame, width=3, font=('Arial', 18), justify='center')
                cell.grid(row=row, column=col, padx=5, pady=5)
                self.cells[(row, col)] = cell

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, pady=10)

        self.check_button = tk.Button(button_frame, text="Check Solution", command=self.check_solution)
        self.check_button.grid(row=0, column=0, padx=5)
        
        self.solve_button = tk.Button(button_frame, text="Solve Puzzle", command=self.solve_puzzle)
        self.solve_button.grid(row=0, column=1, padx=5)

        self.clear_button = tk.Button(button_frame, text="Clear Board", command=self.clear_board)
        self.clear_button.grid(row=0, column=2, padx=5)
        
        self.reset_button = tk.Button(button_frame, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=0, column=3, padx=5)
        
        self.difficulty_var = tk.StringVar(value='easy')
        difficulty_frame = tk.Frame(self.root)
        difficulty_frame.grid(row=2, column=0, pady=10)

        tk.Label(difficulty_frame, text="Difficulty:").pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text='Easy', variable=self.difficulty_var, value='easy', command=self.set_difficulty).pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text='Medium', variable=self.difficulty_var, value='medium', command=self.set_difficulty).pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text='Hard', variable=self.difficulty_var, value='hard', command=self.set_difficulty).pack(side=tk.LEFT)

    def set_difficulty(self):
        self.difficulty = self.difficulty_var.get()
        self.reset_game()

    def read_board(self):
        for row in range(9):
            for col in range(9):
                try:
                    value = int(self.cells[(row, col)].get()) if self.cells[(row, col)].get() else 0
                    if value < 0 or value > 9:
                        raise ValueError
                    self.sudoku.board[row][col] = value
                except ValueError:
                    messagebox.showerror("Error", "Invalid input! Please enter numbers between 1 and 9.")
                    return False
        return True

    def check_solution(self):
        if self.read_board():
            if self.sudoku.is_valid_solution():
                self.show_solution_steps()
                messagebox.showinfo("Success", "Congratulations! You solved the Sudoku puzzle.")
            else:
                messagebox.showerror("Error", "The solution is incorrect. Please try again.")

    def show_solution_steps(self):
        steps = self.sudoku.steps
        step_strings = []
        if steps:
            for row, col, num in steps:
                if num:
                    step_strings.append(f"Cell ({row}, {col}) set to {num}")
                else:
                    step_strings.append(f"Cell ({row}, {col}) reset")
        else:
            step_strings.append("No steps were taken to solve the puzzle.")

        self.create_popup("Solution Steps", "\n".join(step_strings))

    def create_popup(self, title, text):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("400x300")
        popup.resizable(False, False) 

        text_area = scrolledtext.ScrolledText(popup, wrap=tk.WORD)
        text_area.insert(tk.END, text)
        text_area.pack(expand=True, fill=tk.BOTH)
        text_area.configure(state='disabled')
            
    def solve_puzzle(self):
        if self.read_board():
            if self.sudoku.solve():
                self.update_gui_with_solution()
            else:
                messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

    def update_gui_with_solution(self):
        for row in range(9):
            for col in range(9):
                self.cells[(row, col)].delete(0, tk.END)
                self.cells[(row, col)].insert(0, str(self.sudoku.board[row][col]))

    def clear_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[(row, col)].delete(0, tk.END)

    def reset_game(self):
        self.sudoku.initialize_board()
        self.clear_board()
        self.sudoku.fill_board_with_puzzle(self.difficulty)