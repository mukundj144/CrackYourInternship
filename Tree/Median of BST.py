def inorder(root, nodes):
    if root is None:
        return
    inorder(root.left, nodes)
    nodes.append(root.data)
    inorder(root.right, nodes)   
    
def findMedian(root):
    nodes = []
    inorder(root, nodes)
    
    n = len(nodes)
    if n % 2 == 1:  # Odd number of nodes
        return nodes[n // 2]
    else:  # Even number of nodes
        median = (nodes[n // 2 - 1] + nodes[n // 2]) / 2
        return int(median) if median.is_integer() else median