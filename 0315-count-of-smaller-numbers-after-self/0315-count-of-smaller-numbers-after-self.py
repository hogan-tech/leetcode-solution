# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class SegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.segTree = [0 for _ in range(4 * size)]

    def update(self, idx: int, val: int, nodeIdx=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.segTree[nodeIdx] += val
            return

        mid = (start + end) // 2
        leftIdx = 2 * nodeIdx + 1
        rightIdx = 2 * nodeIdx + 2

        if idx <= mid:
            self.update(idx, val, leftIdx, start, mid)
        else:
            self.update(idx, val, rightIdx, mid + 1, end)

        self.segTree[nodeIdx] = self.segTree[leftIdx] + self.segTree[rightIdx]

    def query(self, left: int, right: int, nodeIdx=0, start=0, end=None) -> int:
        if end is None:
            end = self.n - 1
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.segTree[nodeIdx]

        mid = (start + end) // 2
        leftIdx = 2 * nodeIdx + 1
        rightIdx = 2 * nodeIdx + 2
        return self.query(left, right, leftIdx, start, mid) + self.query(left, right, rightIdx, mid + 1, end)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        sortedNums = sorted(set(nums))
        rankMap = {val: idx for idx, val in enumerate(sortedNums)}

        tree = SegmentTree(len(sortedNums))
        result = []

        for num in reversed(nums):
            idx = rankMap[num]
            result.append(tree.query(0, idx - 1))
            tree.update(idx, 1)

        return result[::-1]


nums = [5, 2, 6, 1]
print(Solution().countSmaller(nums))  
nums = [-1]
print(Solution().countSmaller(nums))  
nums = [-1, -1]
print(Solution().countSmaller(nums))  
