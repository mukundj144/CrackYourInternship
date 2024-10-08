# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output=[]
        self.inorder(root,output)

        return output   

    def inorder(self,root,output):
        if not root:
            return
        self.inorder(root.left,output)
        output.append(root.val)
        self.inorder(root.right,output)
     

        