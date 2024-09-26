from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if root is None:
            return []

        def levelOrder(node: Optional[TreeNode], level: int):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                levelOrder(node.left, level + 1)
            if node.right:
                levelOrder(node.right, level + 1)

        levelOrder(root, 0)

        for i in range(len(levels)):
            if i % 2:
                levels[i].reverse()
        return levels


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().zigzagLevelOrder(root))
