from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []

        def isLeaf(node: Optional[TreeNode]) -> bool:
            nonlocal result
            if node is None:
                return False
            if node.left is None and node.right is None:
                return True

        def addLeftBound(node: TreeNode):
            nonlocal result
            while node:
                if not isLeaf(node):
                    result.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def addRightBound(node: TreeNode):
            nonlocal result
            stack = []
            while node:
                if not isLeaf(node):
                    stack.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            result += stack[::-1]

        def addLeaf(node: TreeNode):
            nonlocal result
            if node:
                if isLeaf(node):
                    result.append(node.val)
                else:
                    addLeaf(node.left)
                    addLeaf(node.right)

        if not isLeaf(root):
            result.append(root.val)
        
        addLeftBound(root.left)
        addLeaf(root)
        addRightBound(root.right)

        return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(Solution().boundaryOfBinaryTree(root))
