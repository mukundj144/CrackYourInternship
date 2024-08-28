class Solution:
    def maxPathSum(self, root):
        # Initialize res as zero
        self.res = float('-inf')  # Initializing with negative infinity

        # Helper function to perform DFS
        def dfs(root):
            if not root:
                return 0
            
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            # Compute max path sum WITH split
            self.res = max(self.res, root.val + leftMax + rightMax)
            
            # Return the maximum sum achievable from the current node downwards
            return root.val + max(leftMax, rightMax)

        # Start the DFS
        dfs(root)
        return self.res  # Return the computed maximum path sum