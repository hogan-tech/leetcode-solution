# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        result = 0
        level = 0

        q = deque()
        q.append(root)

        while q:
            level += 1
            sumAtCurrLevel = 0
            for _ in range(len(q)):
                node = q.popleft()
                sumAtCurrLevel += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if maxSum < sumAtCurrLevel:
                maxSum = sumAtCurrLevel
                result = level
        return result


root = TreeNode(1)
root.left = TreeNode(7)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
root.right = TreeNode(0)
print(Solution().maxLevelSum(root))
