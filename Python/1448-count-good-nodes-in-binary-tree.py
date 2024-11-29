class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def traverse(node: TreeNode, maxSoFar: int):
            nonlocal count
            if node is None:
                return None
            if node.val >= maxSoFar:
                count += 1
            traverse(node.left, max(node.val,maxSoFar))
            traverse(node.right, max(node.val,maxSoFar))

        traverse(root, -float('inf'))
        return count


root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
print(Solution().goodNodes(root))
