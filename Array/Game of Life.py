class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS=len(board)
        COLS=len(board[0])
        def countneigh(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),                         (1, 1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in [1, 3]:  # 3 means the cell was alive and stays alive
                    count += 1
            return count

        for r in range(ROWS):
            for c in range(COLS):
                nei=countneigh(r,c)
                if board[r][c]:
                    if nei in [2,3]:
                        board[r][c]=3
                elif nei==3:
                    board[r][c]=2

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==1:
                    board[r][c]=0
                elif board[r][c] in [2,3]:
                    board[r][c]=1    


            