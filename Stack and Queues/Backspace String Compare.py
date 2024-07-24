class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        ans1, ans2 = [], []

        # Process the first string
        for i in range(m):
            if s[i] != '#':
                ans1.append(s[i])
            elif ans1:
                ans1.pop()

        # Process the second string
        for i in range(n):
            if t[i] != '#':
                ans2.append(t[i])
            elif ans2:
                ans2.pop()

        ''.join(ans1)
        ''.join(ans2)

        return ans1 == ans2

