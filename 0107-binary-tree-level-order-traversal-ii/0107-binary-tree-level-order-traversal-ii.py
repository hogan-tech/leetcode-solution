# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def helper(node, level):
            if not node:
                return
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        return result[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrderBottom(root))
