# Sudoku Solver with GUI

This is a simple Sudoku solver with a graphical user interface (GUI) built using Tkinter in Python. The application allows users to input numbers into the Sudoku grid and either check their solution, view the steps taken to solve it, or automatically solve the puzzle.

## Features

- **Input Sudoku Puzzle**: Users can enter their own Sudoku puzzles.
- **Check Solution**: Validates the user’s solution and shows the steps taken to solve the puzzle.
- **Solve Puzzle**: Automatically solves the Sudoku puzzle using a backtracking algorithm.
- **Difficulty Levels**: Allows selection of puzzle difficulty (Easy, Medium, Hard).

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your system.
3. Run the script using the command:
    ```bash
    python main.py
    ```

## Usage

1. **Enter Puzzle**: Click on the cells and enter numbers (1-9) to set up your Sudoku puzzle.
2. **Check Solution**: Click the "Check Solution" button to validate your input solution. If the solution is incorrect, steps taken to solve the puzzle will be displayed.
3. **View Solution Steps**: After checking the solution, a detailed view of the steps taken to solve the puzzle will be shown.
4. **Solve Puzzle**: Click the "Solve Puzzle" button to automatically solve the puzzle.
5. **Clear Board**: Click the "Clear Board" button to reset the grid.
6. **Reset Game**: Click the "Reset Game" button to reset the game to its initial state with a new puzzle based on the selected difficulty.
7. **Difficulty Levels**: Select the desired difficulty level (Easy, Medium, Hard) using the radio buttons. The puzzle will be adjusted accordingly when the game is reset.

## License

This project is licensed under the MIT License.
