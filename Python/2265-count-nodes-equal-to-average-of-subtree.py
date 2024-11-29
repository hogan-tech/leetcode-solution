from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def traverse(node):
            nonlocal result

            if not node:
                return 0, 0

            leftSum, leftCount = traverse(node.left)
            rightSum, rightCount = traverse(node.right)

            currSum = node.val + leftSum + rightSum
            currCount = 1 + leftCount + rightCount

            if currSum // currCount == node.val:
                result += 1

            return currSum, currCount

        traverse(root)
        return result


root = TreeNode(4)
root.left = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(6)


print(Solution().averageOfSubtree(root))
