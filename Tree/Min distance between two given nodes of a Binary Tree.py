
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self, root, a, b):
        # Function to find the LCA of two nodes in a binary tree (general case)
        def find_lca(node, a, b):
            if node is None:
                return None
            if node.data == a or node.data == b:
                return node

            left_lca = find_lca(node.left, a, b)
            right_lca = find_lca(node.right, a, b)

            if left_lca and right_lca:
                return node
            return left_lca if left_lca else right_lca
        
        # To find the distance of node from lca
        def height(root, x):
            if root is None:
                return float('inf') 
            if root.data == x:
                return 0
            
            return 1 + min(height(root.left, x), height(root.right, x))

        # Find the LCA of the nodes a and b
        ancestor = find_lca(root, a, b)

        # Find the distance from LCA to node a and node b using the height function
        h1 = height(ancestor, a)
        h2 = height(ancestor, b)

        # Return the sum of distances from LCA to a and b
        return h1 + h2