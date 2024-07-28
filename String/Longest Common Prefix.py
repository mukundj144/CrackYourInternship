class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]

        for i in range(min(len(first),len(last))): #for having the word or string to be common it should lie in both the words which are getting compared  so the minimum number of tranverse it will do 
            if first[i]!=last[i]:
                return ans
            ans+=first[i]

        return ans        