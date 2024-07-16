class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset={}
        for i in range(len(nums)):
            hashset[nums[i]]=1+hashset.get(nums[i],0)

        for num in hashset:
            if hashset[num]>len(nums)//2:
                return num  