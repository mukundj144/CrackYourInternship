# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0

            left_depth = depth(root.left)
            right_depth = depth(root.right)

            # Update the diameter when traversing each node
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the depth of the subtree rooted at this node
            return 1 + max(left_depth, right_depth)

        self.diameter = 0  # Initialize diameter as a class variable
        depth(root)
        return self.diameter
        