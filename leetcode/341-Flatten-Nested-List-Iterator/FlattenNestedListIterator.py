# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        flattenList = []

        def flatten(nint):
            if nint.isInteger():
                return [nint.getInteger()]
            else:
                ls = nint.getList()
                res = []
                for i in ls:
                    if type(i) is int:
                        res.append(i)
                    else:
                        res.extend(flatten(i))
                return res

        for nint in nestedList:
            flattenList.extend(flatten(nint))

        self.flattenList = flattenList
        self.nextIdx = 0

    def next(self):
        """
        :rtype: int
        """
        self.nextIdx += 1
        return self.flattenList[self.nextIdx - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextIdx < len(self.flattenList)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
