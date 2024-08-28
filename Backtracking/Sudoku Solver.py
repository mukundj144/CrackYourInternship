class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board, row, col, num):
            # Check the row
            for i in range(len(board)):
                if board[row][i] == num:
                    return False
            
            # Check the column
            for i in range(len(board)):
                if board[i][col] == num:
                    return False
            
            # Check the 3x3 sub-box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            
            return True
        
        def solve(board):
            for row in range(len(board)):
                for col in range(len(board)):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                
                                if solve(board):
                                    return True
                                
                                board[row][col] = '.'
                        return False
            return True
        
        solve(board)
