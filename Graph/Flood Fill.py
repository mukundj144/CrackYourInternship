class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
    
        if starting_color == color:
            return image
    
    # Define the DFS function
        def dfs(x, y):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != starting_color:
                return
        
            image[x][y] = color
        
            # Recursively call DFS on the four directions (up, down, left, right)
            dfs(x + 1, y)  # Down
            dfs(x - 1, y)  # Up
            dfs(x, y + 1)  # Right
            dfs(x, y - 1)  # Left
    
        # Start DFS from the starting pixel
        dfs(sr, sc)
    
        # Return the modified image
        return image