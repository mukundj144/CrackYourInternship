'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def solve(self, root, k, count, path):
        # Base case: if the current node is None, return
        if not root:
            return

        # Add current node's data to the path
        path.append(root.data)

        # Recurse on the left subtree
        self.solve(root.left, k, count, path)
        # Recurse on the right subtree
        self.solve(root.right, k, count, path)

        # Check for k-sum paths
        sum = 0
        for i in range(len(path) - 1, -1, -1):
            sum += path[i]
            if sum == k:
                count[0] += 1

        # Backtrack: remove the current node's data from the path
        path.pop()

    def sumK(self, root, k):
        path = []
        count = [0]
        self.solve(root, k, count, path)
        return count[0]
