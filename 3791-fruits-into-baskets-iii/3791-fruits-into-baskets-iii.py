# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class SegTree:
    def __init__(self, baskets):
        self.n = len(baskets)
        size = 2 << (self.n - 1).bit_length()
        self.segList = [0] * size
        self.build(baskets, 1, 0, self.n - 1)

    def maintain(self, currIdx):
        self.segList[currIdx] = max(self.segList[currIdx * 2], self.segList[currIdx * 2 + 1])

    def build(self, arr, currIdx, left, right):
        if left == right:
            self.segList[currIdx] = arr[left]
            return
        mid = (left + right) // 2
        self.build(arr, currIdx * 2, left, mid)
        self.build(arr, currIdx * 2 + 1, mid + 1, right)
        self.maintain(currIdx)

    def findAndUpdate(self, currIdx, left, right, target):
        if self.segList[currIdx] < target:
            return -1
        if left == right:
            self.segList[currIdx] = -1
            return left
        mid = (left + right) // 2
        i = self.findAndUpdate(currIdx * 2, left, mid, target)
        if i == -1:
            i = self.findAndUpdate(currIdx * 2 + 1, mid + 1, right, target)
        self.maintain(currIdx)
        return i


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        if n == 0:
            return len(fruits)

        segTree = SegTree(baskets)
        result = 0

        for fruit in fruits:
            if segTree.findAndUpdate(1, 0, n - 1, fruit) == -1:
                result += 1

        return result


fruits = [4, 2, 5]
baskets = [3, 5, 4]
print(Solution().numOfUnplacedFruits(fruits, baskets))
fruits = [3, 6, 1]
baskets = [6, 4, 7]
print(Solution().numOfUnplacedFruits(fruits, baskets))
