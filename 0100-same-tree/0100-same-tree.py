# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(2)

print(Solution().isSameTree(p, q))
