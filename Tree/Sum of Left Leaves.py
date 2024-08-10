# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Base case: If the root is None, there are no nodes to process
            if not root:
                return 0
        
            # Check if the left child is a leaf node
            if root.left and not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        
            # Recursively calculate the sum of left leaves in both subtrees
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)