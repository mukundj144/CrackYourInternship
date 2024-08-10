# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result=[]
        quene=[root]

        while quene:
            level_val=[]
            level_size=len(quene)
            for i in range(level_size):
                node=quene.pop(0)
                level_val.append(node.val)

                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)  

            result.append(level_val) 

        return result                 