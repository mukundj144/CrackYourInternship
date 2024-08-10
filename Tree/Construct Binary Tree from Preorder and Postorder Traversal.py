# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        # The first element in preorder is always the root
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        # If there's only one element left, it must be a single node tree
        if not preorder or not postorder:
            return root

        # The next element in preorder is the left child (if it exists)
        left_child_val = preorder[0]
        
        # Find the left child in the postorder list to determine the size of the left subtree
        left_child_idx = postorder.index(left_child_val)
        
        # Use left subtree size to divide preorder and postorder lists for left and right subtrees
        # left subtree (preorder: 1 to left_child_idx+1, postorder: 0 to left_child_idx)
        # right subtree (preorder: left_child_idx+1 to end, postorder: left_child_idx+1 to -2)
        root.left = self.constructFromPrePost(preorder[:left_child_idx + 1], postorder[:left_child_idx + 1])
        root.right = self.constructFromPrePost(preorder[left_child_idx + 1:], postorder[left_child_idx + 1:-1])

        return root
