class Solution:
    def reverseWords(self, s: str) -> str:
        split=s.split()
        first = 0
        last = len(split) - 1
        
        while first < last:
            split[first], split[last] = split[last], split[first]
            first += 1
            last -= 1
        
        result = " ".join(split)
        return result


