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
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSums = [0]
        for num in nums:
            preSums.append(preSums[-1] + num)

        allSums = set()
        for preSum in preSums:
            allSums.add(preSum)
            allSums.add(preSum - lower)
            allSums.add(preSum - upper)

        sortedSums = sorted(allSums)
        rankMap = {val: idx for idx, val in enumerate(sortedSums)}

        tree = SegmentTree(len(sortedSums))
        count = 0

        for preSum in preSums:
            left = rankMap[preSum - upper]
            right = rankMap[preSum - lower]
            count += tree.query(left, right)
            tree.update(rankMap[preSum], 1)

        return count


nums = [-2, 5, -1]
lower = -2
upper = 2
print(Solution().countRangeSum(nums, lower, upper))
nums = [0]
lower = 0
upper = 0
print(Solution().countRangeSum(nums, lower, upper))
