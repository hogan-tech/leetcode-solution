# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodeList = []

        def traverse(node: Optional[TreeNode]):
            nonlocal nodeList
            if node is None:
                return
            nodeList.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        nodeList.sort()
        minDif = float("inf")
        for i in range(1, len(nodeList)):
            minDif = min(minDif, nodeList[i] - nodeList[i-1])
        return minDif


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
print(Solution().getMinimumDifference(root))
