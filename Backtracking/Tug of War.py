from typing import List

class Solution:
    def tug_of_war(self, arr: List[int], n: int, i: int, sum1: int, sum2: int, arr1: List[int], arr2: List[int], diff: List[int], res: List[bool]):
        if i == n:
            if len(arr1) == (n + 1) // 2:
                current_diff = abs(sum1 - sum2)
                if current_diff < diff[0]:
                    diff[0] = current_diff
                    for j in range(n):
                        res[j] = False
                    for index in arr1:
                        res[index] = True
            return
        
        arr1.append(i)
        self.tug_of_war(arr, n, i + 1, sum1 + arr[i], sum2, arr1, arr2, diff, res)
        arr1.pop()
        
        arr2.append(i)
        self.tug_of_war(arr, n, i + 1, sum1, sum2 + arr[i], arr1, arr2, diff, res)
        arr2.pop()
    
    def minDifference(self, n: int, arr: List[int]) -> List[List[int]]:
        diff = [float('inf')]
        res = [False] * n
        self.tug_of_war(arr, n, 0, 0, 0, [], [], diff, res)
        
        sum1, sum2 = 0, 0
        for i in range(n):
            if res[i]:
                sum1 += arr[i]
            else:
                sum2 += arr[i]
        
        # Sort the sums before returning
        return [[sum1], [sum2]] if sum1 < sum2 else [[sum2], [sum1]]
