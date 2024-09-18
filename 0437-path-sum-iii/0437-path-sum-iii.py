# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def traverse(node: TreeNode, currSum: int):
            nonlocal count
            if node is None:
                return
            currSum += node.val
            if currSum == targetSum:
                count += 1

            count += prefixHash[currSum - targetSum]
            prefixHash[currSum] += 1

            traverse(node.left, currSum)
            traverse(node.right, currSum)
            prefixHash[currSum] -= 1

        count = 0
        prefixHash = defaultdict(int)
        traverse(root, 0)
        return count


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
targetSum = 8
print(Solution().pathSum(root, targetSum))
