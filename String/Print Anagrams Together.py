from collections import defaultdict

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of words
        n: number of words
        return : list of groups of anagrams {list will be sorted in driver code (not word in group)}
        '''
        dic = defaultdict(list)

        for word in words:
            sorted_word = "".join(sorted(word))
            dic[sorted_word].append(word)

        return list(dic.values())