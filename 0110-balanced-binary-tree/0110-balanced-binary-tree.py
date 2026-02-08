# time complexity: O(nlogn)
# space complexity: O(n)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def height(self, node: TreeNode):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, node: TreeNode):
        if not node:
            return True
        if abs(self.height(node.left)-self.height(node.right)) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isBalancedHelper(self, root: TreeNode):
        if not root:
            return True, -1

        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().isBalanced(root))
