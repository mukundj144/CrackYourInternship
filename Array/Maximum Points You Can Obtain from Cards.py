class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_left, sum_right = sum(cardPoints[:k]), 0
        res = sum_left
        n=len(cardPoints)
        for i in range(k):
            sum_left -= cardPoints[k-i-1]
            sum_right += cardPoints[n-i-1]
            res = max(res, sum_left + sum_right)
        return res