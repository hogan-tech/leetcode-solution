# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        calculations = []

        def sumInverse(depth: int, nestedList: List[NestedInteger]):
            for integer in nestedList:

                if integer.isInteger():
                    calculations.append((integer.getInteger(), depth))
                else:
                    sumInverse(depth+1, integer.getList())

        sumInverse(1, nestedList)

        if len(calculations) == 0:
            return 0
        maxDepth = max([v for k, v in calculations])

        totalSum = 0

        for value, depth in calculations:
            totalSum += value*(maxDepth-depth+1)

        return totalSum
