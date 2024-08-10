# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Helper function to perform in-order traversal and collect values
        def in_order_traversal(node):
            if node is None:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Get the sorted list of values from in-order traversal
        values = in_order_traversal(root)
        
        # Initialize minimum difference to a large value
        min_diff = float(inf)
        
        # Compute the minimum absolute difference between consecutive values
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])
        
        return min_diff
        
