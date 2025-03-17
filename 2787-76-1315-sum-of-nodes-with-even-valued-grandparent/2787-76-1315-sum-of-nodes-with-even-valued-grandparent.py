# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def traverse(node, parent, grandParent):
            if not node:
                return 0
            return traverse(node.left, node.val, parent) + traverse(node.right, node.val, parent) + (node.val if grandParent % 2 == 0 else 0)

        return traverse(root, -1, -1)


'''
         0
     /      \
    1         2
   / \       / \
  3   4     5   6
 7 8 9 10 11 12 13 14 
'''

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
print(Solution().sumEvenGrandparent(root))
root2 = TreeNode(1)
print(Solution().sumEvenGrandparent(root2))
