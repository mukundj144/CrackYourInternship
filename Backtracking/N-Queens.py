class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(queenNo, j, arr):
            for i in range(queenNo):
                if arr[i] == j or abs(i - queenNo) == abs(arr[i] - j):
                    return False
            return True

        def Nqueen(arr, queenNo, n, solutions):
            if queenNo == n:
                solution = []
                for i in range(n):
                    row = ['.'] * n
                    row[arr[i]] = 'Q'
                    solution.append("".join(row))
                solutions.append(solution)
                return
            for i in range(n):
                if check(queenNo, i, arr):
                    arr[queenNo] = i 
                    Nqueen(arr, queenNo + 1, n, solutions)

        solutions = []
        arr = [-1] * n
        Nqueen(arr, 0, n, solutions)
        return solutions