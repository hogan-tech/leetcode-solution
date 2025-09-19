# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List

class TreeNode:
    def __init__(self, start, end, val=0, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, l, r):
        if l == r:
            return TreeNode(l, r, 0)
        leftTree = self.build(l, (l + r) // 2)
        rightTree = self.build((l + r) // 2 + 1, r)
        return TreeNode(l, r, 0, leftTree, rightTree)

    def update(self, root, index, value):
        if root.start == root.end == index:
            root.val += value
            return root.val
        if root.start > index or root.end < index:
            return root.val
        root.val = self.update(root.left, index, value) + self.update(root.right, index, value)
        return root.val

    def query(self, root, l, r) -> int:
        if root.start > r or root.end < l:
            return 0
        if l <= root.start and root.end <= r:
            return root.val
        return self.query(root.left, l, r) + self.query(root.right, l, r)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        sortedNums = sorted(set(nums))
        rankMap = {val: idx for idx, val in enumerate(sortedNums)}
        tree = SegmentTree(len(sortedNums))
        result = []
        for n in reversed(nums):
            idx = rankMap[n]
            result.append(tree.query(tree.root, 0, idx - 1))
            tree.update(tree.root, idx, 1)
        return result[::-1]

nums = [5, 2, 6, 1]
print(Solution().countSmaller(nums))
nums = [-1]
print(Solution().countSmaller(nums))
nums = [-1, -1]
print(Solution().countSmaller(nums))
