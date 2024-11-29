# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []

        def dfs(node):
            if not node:
                return True, 0, 0
            leftIsPerfect, leftHeight, leftSize = dfs(node.left)
            rightIsPerfect, rightHeight, rightSize = dfs(node.right)
            if leftIsPerfect and rightIsPerfect and leftHeight == rightHeight:
                currSize = leftSize + rightSize + 1
                sizes.append(currSize)
                return True, leftHeight + 1, currSize
            else:
                return False, 0, 0

        dfs(root)

        sizes.sort(reverse=True)

        if len(sizes) >= k:
            return sizes[k - 1]
        else:
            return -1


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(5)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(8)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
k = 2

print(Solution().kthLargestPerfectSubtree(root, k))
