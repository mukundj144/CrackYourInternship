# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left) 
        self.temp.append(node)  
        self.inorder(node.right)  
            
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.temp = []
        if not root:
            return None

        self.inorder(root)  
        srt = sorted(n.val for n in self.temp)  
        
        for i in range(len(srt)):
            self.temp[i].val = srt[i]
