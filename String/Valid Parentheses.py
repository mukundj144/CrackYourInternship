class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        paren={')':'(','}':'{',']':'['}

        for c in s:
            if c in paren:
                if stack and stack[-1]==paren[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                

        