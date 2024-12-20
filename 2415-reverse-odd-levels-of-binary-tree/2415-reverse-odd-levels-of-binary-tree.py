# time complexity: O(n)
# space complexity: O(logn)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(leftChild: Optional[TreeNode], rightChild: Optional[TreeNode], level: int):
            if not leftChild or not rightChild:
                return None
            if level % 2 == 0:
                temp = leftChild.val
                leftChild.val = rightChild.val
                rightChild.val = temp

            traverse(leftChild.left, rightChild.right, level + 1)
            traverse(leftChild.right, rightChild.left, level + 1)

        traverse(root.left, root.right, 0)
        return root


root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)
print(Solution().reverseOddLevels(root))
