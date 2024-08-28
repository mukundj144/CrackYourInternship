from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Dictionary to hold the nodes' values grouped by their column index.
        col_table = defaultdict(list)
        
        # Queue to perform BFS. Stores tuples of (node, row, col).
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            
            if node:
                # Add the node to the col_table
                col_table[col].append((row, node.val))
                
                # Add left and right children to the queue
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        # Sort the dictionary by column, then by row, and by value.
        sorted_columns = sorted(col_table.keys())
        result = []
        
        for col in sorted_columns:
            # Sort first by row, then by value
            col_table[col].sort(key=lambda x: (x[0], x[1]))
            column_values = [val for row, val in col_table[col]]
            result.append(column_values)
        
        return result
