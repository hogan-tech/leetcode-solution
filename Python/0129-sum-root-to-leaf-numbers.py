# time complexity: O(n)
# space complexity: O(h)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> List[int]:
        sumNode = 0

        def traverse(node: Optional[TreeNode], currNum: int):
            nonlocal sumNode
            if node is None:
                return
            currNum = currNum * 10 + node.val
            if node.left is None and node.right is None:
                sumNode += currNum
            traverse(node.left, currNum)
            traverse(node.right, currNum)
        traverse(root, 0)
        return sumNode


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().sumNumbers(root))
