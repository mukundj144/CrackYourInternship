# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, node):
        if not node:
            return None
        self.temp.append(node)    
        self.preorder(node.left)
        self.preorder(node.right)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.temp = []
        if not root:
            return None
        self.preorder(root)
        l = len(self.temp)

        for i in range(1, l):
            self.temp[i-1].right = self.temp[i]
            self.temp[i-1].left = None  # Set the left child to None
           

        self.temp[-1].right = None  # Last node's right child should be None
        self.temp[-1].left = None  # Last node's left child should be None
        
        return self.temp
