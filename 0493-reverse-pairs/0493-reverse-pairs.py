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
        leftTree = self.build(l, (l+r)//2)
        rightTree = self.build((l+r)//2 + 1, r)
        return TreeNode(l, r, 0, leftTree, rightTree)

    def update(self, root, index, value):
        if root.start == root.end == index:
            root.val += value
            return root.val
        if root.start > index or root.end < index:
            return root.val
        root.val = self.update(root.left, index, value) + \
            self.update(root.right, index, value)
        return root.val

    def query(self, root, l, r) -> int:
        if root.start > r or root.end < l:
            return 0
        if l <= root.start and root.end <= r:
            return root.val
        return self.query(root.left, l, r) + self.query(root.right, l, r)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums + [2 * x for x in nums]))
        rankMap = {val: idx for idx, val in enumerate(sortedNums)}

        self.tree = SegmentTree(len(sortedNums))
        result = 0
        for n in reversed(nums):
            result += self.tree.query(self.tree.root, 0, rankMap[n]-1)
            self.tree.update(self.tree.root, rankMap[2*n], 1)
        return result


nums = [1, 3, 2, 3, 1]
print(Solution().reversePairs(nums))
nums = [2, 4, 3, 5, 1]
print(Solution().reversePairs(nums))
