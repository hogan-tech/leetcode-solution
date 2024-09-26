# time complexity: O(n)
# space complexity: O(h)
import statistics
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        result = []
        if root is None:
            return

        def levelOrder(node: TreeNode, level: List[int]):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                levelOrder(node.left, level + 1)
            if node.right:
                levelOrder(node.right, level + 1)

        levelOrder(root, 0)
        for level in levels:
            result.append(statistics.mean(level))

        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().averageOfLevels(root))
