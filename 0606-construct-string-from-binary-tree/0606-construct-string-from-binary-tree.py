from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        self.dfs(root, res)
        return ''.join(res)

    def dfs(self, root: Optional[TreeNode], res: []):
        if root is None:
            return

        res.append(str(root.val))

        if root.left is None and root.right is None:
            return

        res.append('(')
        self.dfs(root.left, res)
        res.append(')')

        if root.right is not None:
            res.append('(')
            self.dfs(root.right, res)
            res.append(')')


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

print(Solution().tree2str(root))
