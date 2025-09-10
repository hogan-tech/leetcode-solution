# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []

        def bfs(node: Optional[TreeNode], level: int):
            if node is None:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)

        bfs(root, 0)
        return result

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            levelLen = len(queue)

            for _ in range(levelLen):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return levels


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
