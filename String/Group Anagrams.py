class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)

        for words in strs:
            sortedlist="".join(sorted(words))
            dic[sortedlist].append(words)
        return dic.values()    
        