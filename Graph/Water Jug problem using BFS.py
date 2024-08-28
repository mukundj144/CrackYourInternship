from collections import deque
import math

class Solution:
    def minSteps(self, m, n, d):
        # Function to check if d liters can be measured using jugs with capacities m and n
        def can_measure(m, n, d):
            if d > max(m, n):
                return False
            return d % math.gcd(m, n) == 0
        
        # If d is not achievable, return -1
        if not can_measure(m, n, d):
            return -1
        
        # BFS initialization
        queue = deque([(0, 0, 0)])  # (amount in jug1, amount in jug2, steps)
        visited = set((0, 0))
        
        while queue:
            jug1, jug2, steps = queue.popleft()
            
            # If either jug has exactly d liters, return the number of steps
            if jug1 == d or jug2 == d:
                return steps
            
            # Generate all possible states from the current state
            next_states = [
                (m, jug2),  # Fill jug1 to its full capacity
                (jug1, n),  # Fill jug2 to its full capacity
                (0, jug2),  # Empty jug1
                (jug1, 0),  # Empty jug2
                (jug1 - min(jug1, n - jug2), jug2 + min(jug1, n - jug2)),  # Pour jug1 -> jug2
                (jug1 + min(jug2, m - jug1), jug2 - min(jug2, m - jug1))   # Pour jug2 -> jug1
            ]
            
            for state in next_states:
                if state not in visited:
                    visited.add(state)
                    queue.append((state[0], state[1], steps + 1))
        
        return -1
