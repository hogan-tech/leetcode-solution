# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        nextLevel = deque([root,])
        while nextLevel:
            currLevel = nextLevel
            nextLevel = deque()
            while currLevel:
                node = currLevel.popleft()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            result.append(node.val)
        return result
    
# DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        def dfs(node: Optional[TreeNode], level: int, rside: List[int]):
            if level == len(rside):
                rside.append(node.val)
            if node.right:
                dfs(node.right, level + 1, rside)
            if node.left:
                dfs(node.left, level + 1, rside)
        dfs(root, 0, result)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().rightSideView(root))
