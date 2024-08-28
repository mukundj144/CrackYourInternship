class Solution:
    def numTrees(self, n: int) -> int:
        dp = {}

        def count_trees(left, right):
            if left > right:
                return 1  # Base case: one possible tree (null)
            if (left, right) in dp:
                return dp[(left, right)]
            
            total_trees = 0
            for val in range(left, right + 1):
                left_trees = count_trees(left, val - 1)
                right_trees = count_trees(val + 1, right)
                total_trees += left_trees * right_trees
            
            dp[(left, right)] = total_trees
            return total_trees
        
        return count_trees(1, n)
