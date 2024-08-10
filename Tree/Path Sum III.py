# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        # Helper function to count paths that start from the current node
        def countPaths(node, target):
            if not node:
                return 0
            
            # Subtract the current node's value from the target
            target -= node.val
            
            # Check if the remaining sum is zero, meaning we've found a valid path
            path_count = 1 if target == 0 else 0
             
            return path_count + countPaths(node.left, target) + countPaths(node.right, target)
        
        # Count paths starting from the current node
        total_paths = countPaths(root, targetSum)
        
        # Recursively check the left and right subtrees
        return total_paths + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)