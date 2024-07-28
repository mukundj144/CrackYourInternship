class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        n = len(nums)
        mod_seen = defaultdict(int)
        mod_seen[0] = 1
        for i in range(n):
            prefix = (prefix + nums[i]) % k
            # Ensure the prefix is non-negative
            if prefix<0:
                prefix+=k
            res += mod_seen[prefix]
            mod_seen[prefix] += 1
        return res