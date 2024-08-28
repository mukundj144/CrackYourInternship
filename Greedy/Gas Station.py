class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff=0
        res=0
        ans=0
        for i in range(len(gas)):
            diff+=(gas[i]-cost[i])
            res+=(gas[i]-cost[i])

            if res<0:
                res=0
                ans=i+1
        if diff<0 or ans>len(gas):
            return -1
        return ans    