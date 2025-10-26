import tkinter as tk
import random
from tkinter import messagebox
import sys
import sqlite3

global userid
userid = sys.argv[1]
print(userid)

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.board = [[0]*9 for _ in range(9)]
        self.solution = [[0]*9 for _ in range(9)]
        self.selected_cell = None
        self.time_elapsed = 0
        self.timer_running = False  # Flag to control timer
        self.timer_label = tk.Label(self.master, text="Time: 00:00")
        self.timer_label.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=450, height=450, borderwidth=0, highlightthickness=0)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.cell_clicked)

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.difficulty_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Difficulty", menu=self.difficulty_menu)
        self.difficulty_menu.add_command(label="Easy", command=lambda: self.new_game("easy", 900))
        self.difficulty_menu.add_command(label="Medium", command=lambda: self.new_game("medium", 720))
        self.difficulty_menu.add_command(label="Hard", command=lambda: self.new_game("hard", 600))

        self.menu.add_command(label="Clear", command=self.clear_board)
        
        self.menu.add_command(label="Submit", command=self.show_score)    

        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        self.solve_button.pack()
        
    def draw_board(self):
        for i in range(10):
            width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(50*i, 0, 50*i, 450, width=width)
            self.canvas.create_line(0, 50*i, 450, 50*i, width=width)

    def clear_board(self):
        self.board = [[0]*9 for _ in range(9)]
        self.canvas.delete("numbers")
        self.timer_running = False  # Stop the timer 
        self.time_elapsed = 0
        self.update_timer()

    def new_game(self, difficulty, countdown):
        self.clear_board()
        self.generate_puzzle()
        self.fill_board(difficulty)
        self.time_elapsed = countdown
        self.timer_running = True  # Start the timer
        self.update_timer()  # Start timer countdown

    def generate_puzzle(self):
        def solve(board):
            empty_cell = find_empty_cell(board)
            if not empty_cell:
                return True
            row, col = empty_cell
            for num in random.sample(range(1, 10), 9):
                if is_valid_move(board, num, (row, col)):
                    board[row][col] = num
                    if solve(board):
                        return True
                    board[row][col] = 0
            return False

        def find_empty_cell(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        return (i, j)
            return None

        def is_valid_move(board, num, pos):
            row, col = pos
            if num in board[row]:
                return False
            if num in [board[i][col] for i in range(9)]:
                return False
            box_x, box_y = col // 3 * 3, row // 3 * 3
            if num in [board[i][j] for i in range(box_y, box_y + 3) for j in range(box_x, box_x + 3)]:
                return False
            return True

        self.board = [[0]*9 for _ in range(9)]
        solve(self.board)
        self.solution = [row[:] for row in self.board]

    def fill_board(self, difficulty):
        num_to_fill = {"easy": 30, "medium": 35, "hard": 45}
        cells_to_empty = random.sample([(i, j) for i in range(9) for j in range(9)], num_to_fill[difficulty])
        for cell in cells_to_empty:
            self.board[cell[0]][cell[1]] = 0

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.canvas.create_text(25 + j * 50, 25 + i * 50, text=str(self.board[i][j]), tags="numbers", font=("Arial", 20))

    def solve(self):
        self.clear_board()
        for i in range(9):
            for j in range(9):
                self.canvas.create_text(25 + j * 50, 25 + i * 50, text=str(self.solution[i][j]), tags="numbers", font=("Arial", 20))

    def submit_board(self, puzzle, solution):   
        score = 0
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == solution[i][j]:
                    score += 1
        return score

    def show_score(self):
        score = self.submit_board(self.board, self.solution)
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        elapsed_time = f"{minutes:02d}:{seconds:02d}"
        var = messagebox.showinfo("Score", f"The score is: {score}\nTime Remaining: {elapsed_time}")
        if var:
             # database
            con = sqlite3.connect("sudoku.db")
            cursor = con.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS game(
                  gameid INTEGER PRIMARY KEY AUTOINCREMENT, 
                  userid INTEGER,
                  score INTEGER,
                  time_elapsed TEXT
            )""")
            cursor.execute("INSERT INTO game(userid,score,time_elapsed)VALUES(?,?,?)",(userid, score, elapsed_time))
            con.commit()
            con.close()
        self.clear_board()

    def cell_clicked(self, event):
        x, y = event.x, event.y
        row, col = y // 50, x // 50
        self.selected_cell = (row, col)

        self.canvas.delete("highlight")
        self.canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, outline="blue", tags="highlight")

        for i in range(9):
            for j in range(9):
                if (i, j) != self.selected_cell:
                    self.canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, outline="", tags="highlight")

        self.canvas.focus_set()  # Set focus on the canvas
        self.canvas.bind("<Key>", self.input_number)

    def input_number(self, event):
        if self.selected_cell:
            try:
                num = int(event.char)
                if 1 <= num <= 9:
                    row, col = self.selected_cell
                    if self.is_valid_move(num, (row, col)):
                        self.board[row][col] = num
                        self.canvas.delete("numbers")
                        for i in range(9):
                            for j in range(9):
                                if self.board[i][j] != 0:
                                    self.canvas.create_text(25 + j * 50, 25 + i * 50, text=str(self.board[i][j]), tags="numbers", font=("Arial", 20))
            except ValueError:
                pass

    def is_valid_move(self, num, pos):
        row, col = pos
        for i in range(9):
            if self.board[i][col] == num and i != row:
                return False
            if self.board[row][i] == num and i != col:
                return False
        box_x, box_y = col // 3 * 3, row // 3 * 3
        for i in range(box_y, box_y + 3):
            for j in range(box_x, box_x + 3):
                if self.board[i][j] == num and (i, j) != (row, col):
                    return False
        return True

    def update_timer(self):
        minutes = self.time_elapsed // 60
        seconds = self.time_elapsed % 60
        time_str = "{:02d}:{:02d}".format(minutes, seconds)
        self.timer_label.config(text="Time: " + time_str)
        
        if self.time_elapsed > 0 and self.timer_running:  # Check if countdown has ended and timer is running
            self.time_elapsed -= 1
            self.master.after(1000, self.update_timer)
        elif self.time_elapsed == 0 and self.timer_running:
            self.timer_running = False
            messagebox.showinfo('Timeout', 'Time is up!')
            self.show_score()

def main():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

#if __name__ == "__main__":
main()
