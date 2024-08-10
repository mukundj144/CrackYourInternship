class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root) != -1  # Return True if balanced, False otherwise

    def check(self, node):
        if not node:
            return 0
        leftHeight = self.check(node.left)
        rightHeight = self.check(node.right)

        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1