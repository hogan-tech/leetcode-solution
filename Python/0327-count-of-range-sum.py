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
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)
        allSums = set()
        for presum in presums:
            allSums.add(presum)
            allSums.add(presum - lower)
            allSums.add(presum - upper)
        sortedSum = sorted(allSums)
        rankMap = {val: idx for idx, val in enumerate(sortedSum)}
        tree = SegmentTree(len(sortedSum))
        result = 0
        for presum in presums:
            left = rankMap[presum - upper]
            right = rankMap[presum - lower]
            result += tree.query(tree.root, left, right)
            tree.update(tree.root, rankMap[presum], 1)
        return result


nums = [-2, 5, -1]
lower = -2
upper = 2
print(Solution().countRangeSum(nums, lower, upper))
nums = [0]
lower = 0
upper = 0
print(Solution().countRangeSum(nums, lower, upper))
