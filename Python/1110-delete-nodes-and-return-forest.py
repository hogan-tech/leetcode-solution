# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], toDelete: List[int]) -> List[TreeNode]:
        result = []
        toDeleteSet = set(toDelete)
        def dfs(node: Optional[TreeNode]):
            nonlocal result
            if node is None:
                return
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in toDeleteSet:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
                return None
            return node
        root = dfs(root)
        if root:
            result.append(root)
        return result


toDelete = [3, 5]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().delNodes(root, toDelete))
