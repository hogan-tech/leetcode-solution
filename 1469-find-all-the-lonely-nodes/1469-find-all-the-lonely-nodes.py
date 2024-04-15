# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node: Optional[TreeNode]):
            if node is None:
                return
            if node.left and node.right is None:
                result.append(node.left.val)
            if node.right and node.left is None:
                result.append(node.right.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)

print(Solution().getLonelyNodes(root))
