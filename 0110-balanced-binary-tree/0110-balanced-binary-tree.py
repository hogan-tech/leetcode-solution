# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def height(self, node: TreeNode):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, node: TreeNode):
        if not node:
            return True
        if abs(self.height(node.left)-self.height(node.right)) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)