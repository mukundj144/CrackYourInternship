from typing import List

class Solution:
    def previous_smaller(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(i)
        
        return ans

    def next_smaller(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [n] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(i)
        
        return ans
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ps = self.previous_smaller(heights)
        ns = self.next_smaller(heights)
        max_area = 0
        
        for i in range(n):
            width = ns[i] - ps[i] - 1
            area = width * heights[i]
            max_area = max(max_area, area)
        
        return max_area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        max_area = 0
        heights = [0] * m
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
