# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def dfs(node, arr):
            if not node:
                return

            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)

        result = []
        dfs(root, result)

        result.sort(key=lambda x: (abs(x - target), x))
        return result[:k]


root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
target = 3.714286
k = 2
print(Solution().closestKValues(root1, target, k))
root2 = TreeNode(1)
target = 0.000000
k = 1
print(Solution().closestKValues(root2, target, k))
