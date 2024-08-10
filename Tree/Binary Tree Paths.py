# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        paths = []
        
        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                # If it's a leaf node, append the path to the paths list
                paths.append("->".join(path))
            else:
                # Continue the search in the left and right children
                dfs(node.left, path)
                dfs(node.right, path)
            
            # Backtrack to explore other paths
            path.pop()
        
        dfs(root, [])
        return paths
