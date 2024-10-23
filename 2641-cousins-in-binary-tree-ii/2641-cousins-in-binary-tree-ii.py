# time complexity: O(n)
# space complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.levelSums = [0] * 100000

    def replaceValueInTree(self, root):
        self.calculateLevelSum(root, 0)
        self.replaceValueInTreeInternal(root, 0, 0)
        return root

    def calculateLevelSum(self, node, level):
        if node is None:
            return
        self.levelSums[level] += node.val
        self.calculateLevelSum(node.left, level + 1)
        self.calculateLevelSum(node.right, level + 1)

    def replaceValueInTreeInternal(self, node, siblingSum, level):
        if node is None:
            return
        leftChildVal = 0 if node.left is None else node.left.val
        rightChildVal = 0 if node.right is None else node.right.val

        if level == 0 or level == 1:
            node.val = 0
        else:
            node.val = self.levelSums[level] - node.val - siblingSum
        self.replaceValueInTreeInternal(
            node.left, rightChildVal, level + 1
        )
        self.replaceValueInTreeInternal(
            node.right, leftChildVal, level + 1
        )


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)
print(Solution().replaceValueInTree(root))
