from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                # Include candidates[i] in the current combination
                path.append(candidates[i])
                # Recursively call backtrack with updated target and path
                backtrack(i + 1, target - candidates[i], path)
                # Backtrack to try the next number
                path.pop()
        
        candidates.sort()  # Sort to handle duplicates and improve efficiency
        result = []
        backtrack(0, target, [])
        return result

