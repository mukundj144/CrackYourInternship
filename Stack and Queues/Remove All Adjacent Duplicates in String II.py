class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Each element in the stack will be a pair [char, count]
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # Remove the element if its count reaches k
            else:
                stack.append([char, 1])
        
        # Reconstruct the string from the stack
        result = []
        for char, count in stack:
            result.append(char * count)
        
        return ''.join(result)
