# Build: O(n) time, O(n) space
# Update: O(log n) time
# sumRange: O(log n) time
# Space usage: O(n)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.segTree = [0 for _ in range(4 * self.n)]
        self.buildTree(nums, 0, 0, self.n - 1)
    
    def buildTree(self, nums, nodeIdx, start, end):
            if start == end:
                self.segTree[nodeIdx] = nums[start]
                return
            leftIdx = 2 * nodeIdx + 1
            rightIdx = 2 * nodeIdx + 2

            mid = (start + end) // 2

            self.buildTree(nums, leftIdx, start, mid)
            self.buildTree(nums, rightIdx, mid + 1, end)

            self.segTree[nodeIdx] = self.segTree[leftIdx] + self.segTree[rightIdx]

    def update(self, index: int, val: int, nodeIdx = 0, start = 0, end = None) -> None:
        if end is None:
            end = self.n - 1
        if start == end:
            self.segTree[nodeIdx] = val
            return
        
        mid = (start + end) // 2
        leftIdx = 2 * nodeIdx + 1
        rightIdx = 2 * nodeIdx + 2

        if index <= mid:
            self.update(index, val, leftIdx, start, mid)
        else:
            self.update(index, val, rightIdx, mid + 1, end)
        
        self.segTree[nodeIdx] = self.segTree[leftIdx] + self.segTree[rightIdx]

    def sumRange(self, left: int, right: int, nodeIdx = 0, start = 0, end = None) -> int:
        if end is None:
            end = self.n - 1
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.segTree[nodeIdx]

        mid = (start + end) // 2
        leftIdx = 2 * nodeIdx + 1
        rightIdx = 2 * nodeIdx + 2
        return self.sumRange(left, right, leftIdx, start, mid) + self.sumRange(left, right, rightIdx, mid + 1, end)


numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))
numArray.update(1, 2)
print(numArray.sumRange(0, 2))
