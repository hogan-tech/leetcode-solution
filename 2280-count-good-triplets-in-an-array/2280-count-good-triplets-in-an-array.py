# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i
        tree = FenwickTree(n)
        res = 0
        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)
            res += left * right
        return res


'''
prefix = [2, 0, 0, 0]
nums = [2, 0, 1, 3]
suffix = [3, 3, 3, 3]
'''
nums1 = [2, 0, 1, 3]
nums2 = [0, 1, 2, 3]
print(Solution().goodTriplets(nums1, nums2))
nums1 = [4, 0, 1, 3, 2]
nums2 = [4, 1, 0, 2, 3]
print(Solution().goodTriplets(nums1, nums2))
