# time complexity: O(n)
# space complexity: O(logn)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        print(node.val, end=" ")
        self.traverse(node.left)
        self.traverse(node.right)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)


nums = [-10, -3, 0, 5, 9]
print(Solution().sortedArrayToBST(nums))
