from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        print(node.val, end=" ")
        self.traverse(node.left)
        self.traverse(node.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getSuccessor(node: TreeNode):
            node = node.right
            while node is not None and node.left is not None:
                node = node.left
            return node

        if root is None:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = getSuccessor(root)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        # self.traverse(root)
        return root


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
key = 3
print(Solution().deleteNode(root, key))
