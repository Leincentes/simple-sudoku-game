import tkinter as tk
from display import SudokuGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()