from collections import deque

class Solution:
    
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                 (2, 1), (1, 2), (-1, 2), (-2, 1)]
        
        def is_valid(x, y):
            return 1 <= x <= N and 1 <= y <= N
        
        start_x, start_y = KnightPos
        target_x, target_y = TargetPos
        
        queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
        visited = [[False] * (N + 1) for _ in range(N + 1)]
        visited[start_x][start_y] = True
        
        while queue:
            x, y, dist = queue.popleft()
            
            # If we reach the target position
            if (x, y) == (target_x, target_y):
                return dist
            
            # Explore all possible moves
            for move in moves:
                new_x, new_y = x + move[0], y + move[1]
                if is_valid(new_x, new_y) and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, dist + 1))
        
        return -1
