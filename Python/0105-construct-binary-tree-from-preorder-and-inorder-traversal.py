# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def arrayToTree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorderIndex
            if left > right:
                return None
            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue)
            preorderIndex += 1
            root.left = arrayToTree(left, inorderMap[rootValue] - 1)
            root.right = arrayToTree(inorderMap[rootValue] + 1, right)
            return root

        preorderIndex = 0
        inorderMap = {}
        for index, value in enumerate(inorder):
            inorderMap[value] = index

        return arrayToTree(0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder))
