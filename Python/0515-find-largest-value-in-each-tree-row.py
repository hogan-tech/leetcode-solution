# time complexity: O(h)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], arr: List[int], level: int):
            if node is None:
                return
            if len(arr) == level:
                arr.append(node.val)
            else:
                arr[level] = max(arr[level], node.val)
            dfs(node.left, arr, level + 1)
            dfs(node.right, arr, level + 1)

        result = []
        dfs(root, result, 0)
        return result


root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(9)

print(Solution().largestValues(root))
