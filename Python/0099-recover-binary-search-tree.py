# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nodeList = []
        binaryList = []

        def inorder(node):
            if not node:
                return
            if node.left:
                inorder(node.left)
            nodeList.append(node.val)
            if node.right:
                inorder(node.right)

        def traverseChange(node):
            if not node:
                return
            currVal = node.val
            currIdx = nodeList.index(currVal)
            node.val = binaryList[currIdx]
            if node.left:
                traverseChange(node.left)
            if node.right:
                traverseChange(node.right)

        inorder(root)
        binaryList = sorted(nodeList)
        traverseChange(root)
        return root


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
print(Solution().recoverTree(root))
