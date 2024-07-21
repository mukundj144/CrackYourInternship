from typing import List

class Solution:
    def previous_smaller(self, heights: List[int]) -> List[int]:
        ans = []
        st = []
        n = len(heights)
        
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            ele = -1 if not st else st[-1]
            ans.append(ele)
            st.append(i)
        
        return ans

    def next_smaller(self, heights: List[int]) -> List[int]:
        ans = []
        st = []
        n = len(heights)
        
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            ele = n if not st else st[-1]
            ans.append(ele)
            st.append(i)
        
        # Reverse to get the correct order
        ans.reverse()
        return ans
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        ps = self.previous_smaller(heights)
        ns = self.next_smaller(heights)
        
        for i in range(n):
            curr = (ns[i] - ps[i] - 1) * heights[i]
            res = max(res, curr)
        
        return res