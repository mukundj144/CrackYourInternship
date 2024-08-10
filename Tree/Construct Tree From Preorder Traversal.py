#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def constructTree(pre, preLN, n):
    # Helper function to construct the tree
    def constructUtil(index):
        if index[0] >= n:
            return None
        
        # Create a new node
        node = Node(pre[index[0]])
        node_type = preLN[index[0]]
        index[0] += 1

        # If the node is not a leaf, recursively construct its left and right children
        if node_type == 'N':
            node.left = constructUtil(index)
            node.right = constructUtil(index)
        
        return node

    # Start constructing the tree from the first index
    return constructUtil([0])

