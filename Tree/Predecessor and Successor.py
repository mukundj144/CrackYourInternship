class Solution:
    def findPreSuc(self, root, pre, suc, key):
        # Base case: if the tree is empty
        if root is None:
            return
        
        # If the key is found at the root
        if root.key == key:
            # Find the predecessor (rightmost child of the left subtree)
            if root.left is not None:
                temp = root.left
                while temp.right:
                    temp = temp.right
                pre.key = temp.key
            
            # Find the successor (leftmost child of the right subtree)
            if root.right is not None:
                temp = root.right
                while temp.left:
                    temp = temp.left
                suc.key = temp.key
            return

        # If the key is smaller than the root's key, go to the left subtree
        if root.key > key:
            suc.key = root.key
            self.findPreSuc(root.left, pre, suc, key)
        else:  # Go to the right subtree
            pre.key = root.key
            self.findPreSuc(root.right, pre, suc, key)
