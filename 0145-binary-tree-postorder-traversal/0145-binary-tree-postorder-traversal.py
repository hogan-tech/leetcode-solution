# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resList = []

        def postorder(node: Optional[TreeNode]):
            if node:
                postorder(node.left)
                postorder(node.right)
                resList.append(node.val)
        postorder(root)
        return resList


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(Solution().postorderTraversal(root))
