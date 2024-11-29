from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if not root:
            return 0

        def dfs(node=root):
            if node is None:
                return (0, 0)
            sumLeft, nodeCntLeft = dfs(node.left)
            sumRight, nodeCntRight = dfs(node.right)
            totalSum = node.val + sumLeft + sumRight
            totalNodes = 1 + nodeCntLeft + nodeCntRight
            average = totalSum / totalNodes
            if average > self.maxAvg:
                self.maxAvg = average
            return (totalSum, totalNodes)
        self.maxAvg = float("-inf")
        dfs()
        return self.maxAvg


root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(1)
print(Solution().maximumAverageSubtree(root))
