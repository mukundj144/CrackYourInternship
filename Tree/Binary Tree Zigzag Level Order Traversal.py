# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result=[]
        countLevel=0
        quene=[root]

        while quene:
            level_val=[]
            countLevel+=1
            level_size=len(quene)
            for i in range(level_size):
                node=quene.pop(0)
                level_val.append(node.val)

                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)  
            if countLevel%2==0:
                level_val.reverse()        
            result.append(level_val) 

        return result
