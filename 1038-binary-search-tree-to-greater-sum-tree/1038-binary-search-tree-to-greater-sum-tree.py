# time complexity: O(n)
# space complexity: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodeSum = [0]
        self.trace(root, nodeSum)
        return root

    def trace(self, node: TreeNode, nodeSum):
        if node is None:
            return
        self.trace(node.right, nodeSum)
        nodeSum[0] += node.val
        node.val = nodeSum[0]
        self.trace(node.left, nodeSum)


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

print(Solution().bstToGst(root))
