# time complexity: O(n)
# space complexity: O(n)
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vecList = nums

    def dotProduct(self, vec: 'SparseVector') -> int:
        newList = vec.vecList
        count = 0
        for i, num in enumerate(newList):
            count += num * self.vecList[i]

        return count


# Your SparseVector object will be instantiated and called as such:
nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))
nums1 = [0, 1, 0, 0, 0]
nums2 = [0, 0, 0, 0, 2]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))
nums1 = [0, 1, 0, 0, 2, 0, 0]
nums2 = [1, 0, 0, 0, 3, 0, 4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))
