class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a node into the BST
def insert_into_bst(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_into_bst(root.left, data)
    else:
        root.right = insert_into_bst(root.right, data)
    return root

# Function to construct a BST from its preorder traversal
def Bst(pre, size) -> Node:
    if size == 0:
        return None
    
    # The first element in preorder is always the root
    root = Node(pre[0])
    
    # Insert remaining elements into the BST
    for i in range(1, size):
        insert_into_bst(root, pre[i])
    
    return root

# Function to perform postorder traversal
def postorder(root, result):
    if root is None:
        return
    
    # Traverse the left subtree
    postorder(root.left, result)
    # Traverse the right subtree
    postorder(root.right, result)
    # Visit the root
    result.append(root.data)

# Function to convert preorder to postorder
def pre_to_post(pre, size):
    # Step 1: Construct the BST from the preorder traversal
    root = Bst(pre, size)
    
    # Step 2: Perform postorder traversal to get postorder sequence
    result = []
    postorder(root, result)
    
    return result
