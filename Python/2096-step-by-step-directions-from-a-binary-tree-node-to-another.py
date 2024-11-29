# time complexity: O(n)
# space complexity: O(n)
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: TreeNode, startValue: int, destValue: int
    ) -> str:
        lowestCommonAncestor = self.findLCA(root, startValue, destValue)
        pathToStart = []
        pathToDest = []
        self.findPath(lowestCommonAncestor, startValue, pathToStart)
        self.findPath(lowestCommonAncestor, destValue, pathToDest)
        directions = []
        directions.extend("U" * len(pathToStart))
        directions.extend(pathToDest)

        return "".join(directions)

    def findLCA(
        self, node: TreeNode, value1: int, value2: int
    ) -> TreeNode:
        if node is None:
            return None
        if node.val == value1 or node.val == value2:
            return node
        leftLCA = self.findLCA(node.left, value1, value2)
        rightLCA = self.findLCA(node.right, value1, value2)
        if leftLCA is None:
            return rightLCA
        elif rightLCA is None:
            return leftLCA
        else:
            return node

    def findPath(
        self, node: TreeNode, targetValue: int, path: List[str]
    ) -> bool:
        if node is None:
            return False
        if node.val == targetValue:
            return True
        path.append("L")
        if self.findPath(node.left, targetValue, path):
            return True
        path.pop()
        path.append("R")
        if self.findPath(node.right, targetValue, path):
            return True
        path.pop()
        return False


startValue = 3
destValue = 6
root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

print(Solution().getDirections(root, startValue, destValue))
