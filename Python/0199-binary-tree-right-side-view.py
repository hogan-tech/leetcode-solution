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
        if not root:
            return result
        def traverse(node, level):
            if len(result) == level:
                result.append(node.val)
            if node.right:
                traverse(node.right, level + 1)
            if node.left:
                traverse(node.left, level + 1)
        traverse(root, 0)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().rightSideView(root))
