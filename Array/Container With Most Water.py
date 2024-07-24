class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            current_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area