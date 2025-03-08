class BingoBoard:
    SIZE = 5
    def __init__(self, x):
        self.board = x
        self.marks = [[False] * self.SIZE for _ in range(self.SIZE)]
    
    def mark_numbers(self, y):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] in y:
                    self.marks[i][j] = True
    
    def is_row_complete(self, row):
        return all(self.marks[row])
    
    def is_column_complete(self, col):
        return all(self.marks[row][col] for row in range(self.SIZE))
    
    def is_main_diagonal_complete(self):
        return all(self.marks[i][i] for i in range(self.SIZE))
    
    def is_anti_diagonal_complete(self):
        return all(self.marks[i][self.SIZE - 1 - i] for i in range(self.SIZE))
    
    def print_board(self):
        for i in range(self.SIZE):
            print("  ".join("X" if self.marks[i][j] else str(self.board[i][j]) for j in range(self.SIZE)))
        print()

class BingoGame:
    LETTERS = ["B", "I", "N", "G", "O"]
    def __init__(self, board, y):
        self.board = board
        self.y = set(y)
        self.bingo_letters = []
    
    def play(self):
        self.board.mark_numbers(self.y)
        completed = 0
        for i in range(BingoBoard.SIZE):
            if self.board.is_row_complete(i):
                completed += 1
            if self.board.is_column_complete(i):
                completed += 1
        if self.board.is_main_diagonal_complete():
            completed += 1
        if self.board.is_anti_diagonal_complete():
            completed += 1
        for _ in range(completed):
            self.strike_letter()
        self.board.print_board()
        self.print_result()
    
    def strike_letter(self):
        if len(self.bingo_letters) < len(self.LETTERS):
            self.bingo_letters.append(self.LETTERS[len(self.bingo_letters)])
    
    def print_result(self):
        if len(self.bingo_letters) == len(self.LETTERS):
            print(" ".join(self.bingo_letters))
            print("Game Completed!")
        else:
            remaining_letters = " ".join(self.LETTERS[len(self.bingo_letters):])
            print(f"Remaining Letters: {remaining_letters}")

def main():
    x = []
    for _ in range(BingoBoard.SIZE):
        row = list(map(int, input().split()))
        x.append(row)
    
    y = list(map(int, input().strip().split(',')))
    
    bingo_board = BingoBoard(x)
    bingo_game = BingoGame(bingo_board, y)
    bingo_game.play()


if __name__ == "__main__":
    main()
