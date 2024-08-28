#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        result = []
        perm = []
        count = {num: 0 for num in arr}

        for num in arr:
            count[num] += 1

        def dfs():
            if len(perm) == len(arr):
                result.append(perm.copy())
                return

            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1

                    dfs()

                    perm.pop()
                    count[num] += 1

        dfs()
        result.sort()
        return result
        