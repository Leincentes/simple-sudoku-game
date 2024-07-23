# Sudoku Solver with GUI

This is a simple Sudoku solver with a graphical user interface (GUI) built using Tkinter in Python. The application allows users to input numbers into the Sudoku grid and either check their solution or automatically solve the puzzle.

## Features

- **Input Sudoku Puzzle**: Users can enter their own Sudoku puzzles.
- **Check Solution**: Validates the user’s solution.
- **Solve Puzzle**: Automatically solves the Sudoku puzzle using a backtracking algorithm.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your system.
3. Run the script using the command:
    ```bash
    python sudoku_game.py
    ```

## Usage

1. **Enter Puzzle**: Click on the cells and enter numbers (1-9) to set up your Sudoku puzzle.
2. **Check Solution**: Click the "Check Solution" button to validate your input solution.
3. **Solve Puzzle**: Click the "Solve Puzzle" button to automatically solve the puzzle.

## Code Structure

- **SudokuGUI Class**: Handles the GUI creation and event handling.
  - `initialize_board()`: Initializes an empty 9x9 Sudoku board.
  - `create_widgets()`: Creates the GUI widgets.
  - `check_solution()`: Checks if the entered solution is valid.
  - `read_board()`: Reads the current board state from the GUI.
  - `is_valid_solution()`: Validates the Sudoku solution.
  - `solve_puzzle()`: Solves the puzzle using a backtracking algorithm.
  - `update_gui_with_solution()`: Updates the GUI with the solved board.
  - `solve()`: Implements the backtracking algorithm to solve the puzzle.
  - `find_empty_location()`: Finds an empty cell in the board.
  - `is_safe()`: Checks if placing a number in a cell is safe.

## Example

Run the script and a window will appear with a 9x9 grid. Enter your Sudoku puzzle into the grid. You can then check if your solution is correct or let the program solve it for you.

## License

This project is licensed under the MIT License.

