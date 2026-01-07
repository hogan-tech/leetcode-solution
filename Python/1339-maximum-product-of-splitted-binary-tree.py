# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        allSums = []

        def treeSum(subroot):
            if subroot is None:
                return 0
            leftSum = treeSum(subroot.left)
            rightSum = treeSum(subroot.right)
            totalSum = leftSum + rightSum + subroot.val
            allSums.append(totalSum)
            return totalSum

        total = treeSum(root)
        result = 0
        for s in allSums:
            result = max(result, s * (total - s))
        return result % (10 ** 9 + 7)
