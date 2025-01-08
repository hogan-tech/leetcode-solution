# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []
        if root is None:
            return []
        def bfs(node: Optional[TreeNode], level: int):
            if len(result) == level:
                result.append([])
            if node is None:
                return
            result[level].append(node.val)
            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)
            
        bfs(root, 0)
        for i, row in enumerate(result):
            if i % 2:
                row.reverse()
        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().zigzagLevelOrder(root))
