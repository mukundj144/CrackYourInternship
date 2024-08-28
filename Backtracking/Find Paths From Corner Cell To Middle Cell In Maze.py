class Solution:
    def ShortestDistance(self, matrix):
        if not matrix or not matrix[0]:
            return [[-1]]

        # Initialize the answer matrix with 0
        ans = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        # Start the recursive maze solver
        if not self.rat_maze(matrix, ans, 0, 0):
            return [[-1]]
        
        return ans

    def within_boundary(self, i, j, matrix):
        if i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0:
            return False
        return True

    def rat_maze(self, matrix, ans, i, j):
        # Check if we've reached the destination
        if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
            ans[i][j] = 1
            return True

        # Check if the current position is within the boundary and valid
        if self.within_boundary(i, j, matrix):
            ans[i][j] = 1
            
            # Explore all possible steps
            for no_of_steps in range(1, matrix[i][j] + 1):
                # Move right
                if self.rat_maze(matrix, ans, i, j + no_of_steps):
                    return True
                # Move down
                if self.rat_maze(matrix, ans, i + no_of_steps, j):
                    return True
            
            # Backtrack
            ans[i][j] = 0
        
        return False