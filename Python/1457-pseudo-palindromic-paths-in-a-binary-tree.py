# time complexity: O(n)
# space complexity: O(h)
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.numPalindromic = 0

        def isPseudoPalindromic(path: dict) -> bool:
            oneOdd = False
            for count in path.values():
                if count % 2 == 1:
                    if oneOdd:
                        return False
                    oneOdd = True
            return True

        def helper(node: Optional[TreeNode], path: dict):
            if node:
                path[node.val] += 1
                if not node.left and not node.right:
                    if isPseudoPalindromic(path):
                        self.numPalindromic += 1
                helper(node.left, path)
                helper(node.right, path)
                path[node.val] -= 1
        helper(root, defaultdict(int))
        return self.numPalindromic


root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.right = TreeNode(1)

print(Solution().pseudoPalindromicPaths(root))
