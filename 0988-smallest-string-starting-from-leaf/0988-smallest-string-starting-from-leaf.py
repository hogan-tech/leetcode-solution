# time complexity: O(n*n)
# space complexity: O(n*n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode], path: List, smallest: List[str]):
            if not node:
                return

            path.append(chr(node.val + ord('a')))

            if not node.left and not node.right:
                currentString = ''.join(path[::-1])
                smallest[0] = min(smallest[0], currentString)

            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)

            path.pop()

        smallest = [chr(ord('z') + 1)]
        dfs(root, [], smallest)
        return smallest[0]


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(Solution().smallestFromLeaf(root))
