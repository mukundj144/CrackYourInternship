class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(index, arrangement):
            if index == n + 1:
                result.append(arrangement[:])
                return
            
            for num in range(1, n + 1):
                if num not in arrangement and (num % index == 0 or index % num == 0):
                    arrangement.append(num)
                    backtrack(index + 1, arrangement)
                    arrangement.pop()
        
        result = []
        backtrack(1, [])
        return len(result)