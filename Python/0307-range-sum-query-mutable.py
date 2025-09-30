# Build: O(n) time, O(n) space
# Update: O(log n) time
# sumRange: O(log n) time
# Space usage: O(n)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0 for _ in range(4 * self.n)]
        self.buildTree(nums, 0, 0, self.n - 1)

    def buildTree(self, nums: List[int], nodeIdx: int, start: int, end: int):
        if start == end:
            self.tree[nodeIdx] = nums[start]
            return
        mid = (start + end) // 2
        self.buildTree(nums, 2 * nodeIdx + 1, start, mid)
        self.buildTree(nums, 2 * nodeIdx + 2, mid + 1, end)
        self.tree[nodeIdx] = self.tree[2 * nodeIdx + 1] + \
            self.tree[2 * nodeIdx + 2]

    def update(self, index: int, val: int, nodeIdx=0, start=0, end=None) -> None:
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[nodeIdx] = val
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, val, 2 * nodeIdx + 1, start, mid)
        else:
            self.update(index, val, 2 * nodeIdx + 2, mid + 1, end)
        self.tree[nodeIdx] = self.tree[2 * nodeIdx + 1] + \
            self.tree[2 * nodeIdx + 2]

    def sumRange(self, left: int, right: int, nodeIdx=0, start=0, end=None) -> int:
        if end is None:
            end = self.n - 1
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[nodeIdx]
        mid = (start + end) // 2
        return self.sumRange(left, right, 2 * nodeIdx + 1, start, mid) + \
            self.sumRange(left, right, 2 * nodeIdx + 2, mid + 1, end)


numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))
numArray.update(1, 2)
print(numArray.sumRange(0, 2))
