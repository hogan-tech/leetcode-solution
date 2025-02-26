# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def traverse(node):
            nonlocal count
            if not node:
                return True
            isLeftUnivalue = traverse(node.left)
            isRightUnivalue = traverse(node.right)

            if isLeftUnivalue and isRightUnivalue:
                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False

                count += 1
                return True
        traverse(root)
        return count


root1 = TreeNode(5)
root1.left = TreeNode(1)
root1.right = TreeNode(5)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(5)
print(Solution().countUnivalSubtrees(root1))
root2 = TreeNode(None)
print(Solution().countUnivalSubtrees(root2))
