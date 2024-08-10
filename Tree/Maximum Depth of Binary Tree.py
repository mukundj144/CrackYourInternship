# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        else:
            l_height=self.maxDepth(root.left)
            r_height=self.maxDepth(root.right)

        if l_height>r_height:
            return l_height+1
        else:
            return r_height+1        

        