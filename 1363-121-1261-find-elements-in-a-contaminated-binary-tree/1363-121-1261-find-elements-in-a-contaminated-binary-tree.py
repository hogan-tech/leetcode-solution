# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        def traverse(node, idx):
            if not node:
                return
            node.val = idx
            if node.left:
                traverse(node.left, 2 * idx + 1)
            if node.right:
                traverse(node.right, 2 * idx + 2)

        traverse(self.root, 0)

    def find(self, target: int) -> bool:
        found = False

        def findNode(node):
            nonlocal found
            if not node:
                return
            if node.val == target:
                found = True
            if node.left:
                findNode(node.left)
            if node.right:
                findNode(node.right)

        findNode(self.root)

        return found


root1 = TreeNode(-1)
root1.right = TreeNode(-1)
findElements1 = FindElements(root1)
print(findElements1.find(1))
print(findElements1.find(2))
root2 = TreeNode(-1)
root2.left = TreeNode(-1)
root2.left.left = TreeNode(-1)
root2.left.right = TreeNode(-1)
root2.right = TreeNode(-1)
findElements2 = FindElements(root2)
print(findElements2.find(1))
print(findElements2.find(2))
