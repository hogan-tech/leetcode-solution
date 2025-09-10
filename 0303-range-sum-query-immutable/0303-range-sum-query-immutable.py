# time complexity: O(1)
# space complexity: O(n)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefixSum[i + 1] = self.prefixSum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]

# Build: O(n) time, O(n) space
# Update: O(log n) time
# sumRange: O(log n) time
# Space usage: O(n)
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.segTree = [0 for _ in range(4 * self.n)]
        self.buildTree(0, 0, self.n - 1, nums)  

    def buildTree(self, idx, start, end, nums):
        if start == end:
            self.segTree[idx] = nums[end]
            return
        mid = (start + end) // 2
        leftChildIdx = 2 * idx + 1
        rightChildIdx = 2 * idx + 2

        self.buildTree(leftChildIdx, start, mid, nums)
        self.buildTree(rightChildIdx, mid+1, end, nums)

        self.segTree[idx] = self.segTree[leftChildIdx] + \
            self.segTree[rightChildIdx]

    def rangeSumQuery(self, idx, left, right, start, end):
        if left >= start and right <= end:
            return self.segTree[idx]
        if right < start or left > end:
            return 0
        leftChildIdx = 2*idx+1
        rightChildIdx = 2*idx+2
        mid = (right+left) // 2
        leftSum = self.rangeSumQuery(leftChildIdx, left, mid, start, end)
        rightSum = self.rangeSumQuery(rightChildIdx, mid+1, right, start, end)

        return leftSum + rightSum

    def sumRange(self, left: int, right: int) -> int:
        return self.rangeSumQuery(0, 0, self.n-1, left, right)


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
