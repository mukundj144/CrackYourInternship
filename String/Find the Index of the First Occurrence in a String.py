class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is an empty string, return 0
        if not needle:
            return 0
        
        # Loop through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check the substring from i to i+len(needle)
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # If needle is not found, return -1
        return -1
