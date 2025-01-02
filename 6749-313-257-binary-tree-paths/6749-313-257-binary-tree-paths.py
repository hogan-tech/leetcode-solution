# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def backtrack(node: Optional[TreeNode], path: str):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    result.append(path)
                else:
                    path += "->"
                    backtrack(node.left, path)
                    backtrack(node.right, path)
        backtrack(root, "")
        return result


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
print(Solution().binaryTreePaths(root1))
root2 = TreeNode(1)
print(Solution().binaryTreePaths(root2))
