from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        def traverse(node: Optional[TreeNode], isLeft: bool):
            if node.left == None and node.right == None:
                return node.val if isLeft else 0
            leftSum = 0
            if node.left:
                leftSum += traverse(node.left, True)
            if node.right:
                leftSum += traverse(node.right, False)
            return leftSum
        return traverse(root, False)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().sumOfLeftLeaves(root))
