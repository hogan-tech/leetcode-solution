# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def longestPath(root: TreeNode) -> List[int]:
            nonlocal maxval

            if not root:
                return [0, 0]

            increase = decrease = 1
            if root.left:
                left = longestPath(root.left)
                if (root.val == root.left.val + 1):
                    decrease = left[1] + 1
                elif (root.val == root.left.val - 1):
                    increase = left[0] + 1

            if root.right:
                right = longestPath(root.right)
                if (root.val == root.right.val + 1):
                    decrease = max(decrease, right[1] + 1)
                elif (root.val == root.right.val - 1):
                    increase = max(increase, right[0] + 1)

            maxval = max(maxval, decrease + increase - 1)
            return [increase, decrease]

        maxval = 0
        longestPath(root)
        return maxval


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
print(Solution().longestConsecutive(root))
