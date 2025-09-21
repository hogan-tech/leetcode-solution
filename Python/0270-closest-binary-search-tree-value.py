# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result = root.val
        minDis = abs(root.val - target)

        def traverse(node):
            nonlocal result
            nonlocal minDis
            if not node:
                return
            currDis = abs(node.val - target)
            if currDis == minDis:

                result = min(result, node.val)
            if currDis < minDis:
                minDis = currDis
                result = node.val
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)
        return result


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
target = 3.714268
print(Solution().closestValue(root, target))
