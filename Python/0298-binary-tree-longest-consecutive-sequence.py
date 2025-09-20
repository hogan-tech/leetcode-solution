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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        result = 0
        while queue:
            node, count = queue.popleft()
            result = max(result, count)
            for nextNode in (node.left, node.right):
                if nextNode:
                    if nextNode.val == node.val + 1:
                        queue.append((nextNode, count + 1))
                    else:
                        queue.append((nextNode, 1))
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
print(Solution().longestConsecutive(root))
