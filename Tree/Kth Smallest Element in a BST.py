# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = [0]  # Counter to keep track of visited nodes
        result = [0]  # Store the kth smallest element
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return result[0] 