# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        nodeSum = []

        def traverse(node: Optional[TreeNode]):
            if node is None:
                return 0
            nodeSum.append(node.val + traverse(node.left) +
                           traverse(node.right))
            return nodeSum[-1]

        total = traverse(root)
        nodeSum.pop()
        return total / 2.0 in nodeSum



'''
    5
   / \
  10 10
    /  \
   2   3
   
[2, 3, 15, 10, 30]

'''
root = TreeNode(5)
root.left = TreeNode(10)
root.right = TreeNode(10)
root.right.left = TreeNode(2)
root.right.right = TreeNode(3)
print(Solution().checkEqualTree(root))
