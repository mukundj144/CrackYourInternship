class Solution:
    def convert(self, board):
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def isValid(self, i, j, n, m, board):
        return 0 <= i < n and 0 <= j < m and board[i][j] == 'O'
    
    def dfs(self, board, i, j, n, m):
        board[i][j] = 'B'
        
        if self.isValid(i + 1, j, n, m, board):
            self.dfs(board, i + 1, j, n, m)
        if self.isValid(i - 1, j, n, m, board):
            self.dfs(board, i - 1, j, n, m)
        if self.isValid(i, j + 1, n, m, board):
            self.dfs(board, i, j + 1, n, m)
        if self.isValid(i, j - 1, n, m, board):
            self.dfs(board, i, j - 1, n, m)
    
    def solve(self, board):
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            # left -> top bottom
            j = 0
            if board[i][j] == 'O':
                self.dfs(board, i, j, n, m)
            
            j = m - 1
            # right -> top bottom
            if board[i][j] == 'O':
                self.dfs(board, i, j, n, m)
        
        for j in range(m):
            # top -> left right
            i = 0
            if board[i][j] == 'O':
                self.dfs(board, i, j, n, m)
            
            i = n - 1
            # bottom -> left right
            if board[i][j] == 'O':
                self.dfs(board, i, j, n, m)
        
        self.convert(board)
