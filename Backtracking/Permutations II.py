class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        count = {num: 0 for num in nums}

        for num in nums:
            count[num] += 1

        def dfs():
            if len(perm) == len(nums):
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
        return result