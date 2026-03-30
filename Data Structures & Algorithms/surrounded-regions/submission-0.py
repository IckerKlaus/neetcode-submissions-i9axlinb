class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def convert(r, c):
            if (r not in range(ROWS) or 
                c not in range(COLS) or
                board[r][c] != "O"):
                return
            board[r][c] = "T"
            convert(r - 1, c)
            convert(r + 1, c)
            convert(r, c - 1)
            convert(r, c + 1)

        # Update O not surrounded in T
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or
                    c in [0, COLS - 1] and
                    board[r][c] == "O"):
                    convert(r, c)
        
        # Update O surrounded in X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Update T in O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"