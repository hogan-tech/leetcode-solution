# time complexity: O(n^2)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode, remainingSum: int, pathNode: List[int], result: List[List[int]]):
        if node is None:
            return
        pathNode.append(node.val)
        if node.val == remainingSum and node.left is None and node.right is None:
            result.append(list(pathNode))
        else:
            self.helper(node.left, remainingSum - node.val, pathNode, result)
            self.helper(node.right, remainingSum - node.val, pathNode, result)
        pathNode.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.helper(root, targetSum, [], result)
        return result


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
targetSum = 22
print(Solution().pathSum(root, targetSum))
