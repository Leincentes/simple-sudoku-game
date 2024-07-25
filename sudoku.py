import random

class Sudoku:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.steps = []  # Track the steps for solving the puzzle

    def initialize_board(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.steps = []  # Reset steps on initialization

    def is_valid_solution(self):
        return (self.is_valid_rows() and 
                self.is_valid_cols() and 
                self.is_valid_boxes())

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

    def solve(self):
        self.steps = []  # Reset steps
        result = self._solve()
        return result

    def _solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                self.steps.append((row, col, num))  # Log the step
                if self._solve():
                    return True
                self.board[row][col] = 0
                self.steps.append((row, col, 0))  # Log the backtrack
        return False

    def find_empty_location(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_safe(self, row, col, num):
        return (self.is_safe_in_row(row, num) and 
                self.is_safe_in_col(col, num) and 
                self.is_safe_in_box(row - row % 3, col - col % 3, num))

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

    def fill_board_with_puzzle(self, difficulty):
        difficulty_levels = {'easy': 20, 'medium': 30, 'hard': 40}
        number_of_puzzles = difficulty_levels.get(difficulty, 20)

        for _ in range(number_of_puzzles):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
            self.board[row][col] = num