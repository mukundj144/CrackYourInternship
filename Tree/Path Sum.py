# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Check if the current node is a leaf
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Subtract the current node's value from the target sum
        targetSum -= root.val
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
