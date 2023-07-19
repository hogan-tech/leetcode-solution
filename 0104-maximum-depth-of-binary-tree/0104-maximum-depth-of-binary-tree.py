# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def longestPath(node: Optional[TreeNode]):
            if not node:
                return 0
            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)
            return max(leftPath, rightPath)+1

        return longestPath(root)