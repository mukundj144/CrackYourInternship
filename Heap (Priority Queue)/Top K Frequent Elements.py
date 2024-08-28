class Solution(object):
    def topKFrequent(self, nums, k):
        count_map = {}
        freq=[[] for i in range(len(nums)+1)]

        # Count the frequency of each number and store it in the hashmap
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        
        for num,count in count_map.items():
            freq[count].append(num)
            
            
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res            