class Solution(object):
    def largestBst(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def isValidBST(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.data
            if val <= lower or val >= upper:
                return False

            if not isValidBST(node.right, val, upper):
                return False
            if not isValidBST(node.left, lower, val):
                return False

            return True
        
        def countNodes(node):
            if not node:
                return 0
            return 1 + countNodes(node.left) + countNodes(node.right)
        
        def findLargestBST(node):
            if not node:
                return 0
            
            if isValidBST(node):
                return countNodes(node)
            
            # Recur for left and right subtrees
            left_size = findLargestBST(node.left)
            right_size = findLargestBST(node.right)
            
            # Return the maximum size of a valid BST subtree
            return max(left_size, right_size)

        return findLargestBST(root)