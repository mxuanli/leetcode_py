# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:

    def __init__(self, nestedList: NestedInteger):
        self.nestedList_c = list()
        self.foo(nestedList, self.nestedList_c)

    def foo(self, nestedList, nestedList_c):
        for nested in nestedList:
            if nested.getInteger():
                nestedList_c.append(nested.getInteger())
            if isinstance(nested, list):
                self.foo(nested.getList(), nestedList_c)
        return

    def next(self) -> int:
        r = self.nestedList_c[0]
        self.nestedList_c = self.nestedList_c[1:]
        return r

    def hasNext(self) -> bool:
        if len(self.nestedList_c) == 0:
            return False
        return True


nestedList = [[1, 1], 2, [1, 1]]
n = NestedIterator(nestedList)
print(n.next())
print(n.next())
print(n.next())
