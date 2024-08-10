# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.output = []
        self.i = 0
        self.helper(nestedList)

    def helper(self, nestedList):
        for nested in nestedList:
            if nested.isInteger():
                self.output.append(nested.getInteger())
            else:
                self.helper(nested.getList())

    def next(self):
        ans = self.output[self.i]
        self.i += 1
        return ans

    def hasNext(self):
        return self.i < len(self.output)

# Assuming NestedInteger is defined somewhere else as described
# The NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
