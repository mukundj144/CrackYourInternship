# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def isIdentical(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            return self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right)
        return False

    def isSubtree(self, root, subRoot):
        root_count = self.countNodes(root)
        subRoot_count = self.countNodes(subRoot)

        if subRoot_count > root_count:
            return False

        if self.isIdentical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)    