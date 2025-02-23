# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class Solution:
    def __init__(self):
        self.preIdx = 0
        self.postIdx = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.constructTree(preorder, postorder)

    def constructTree(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.preIdx])
        self.preIdx += 1

        if root.val != postorder[self.postIdx]:
            root.left = self.constructTree(preorder, postorder)

        if root.val != postorder[self.postIdx]:
            root.right = self.constructTree(preorder, postorder)

        self.postIdx += 1
        return root


preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
print(Solution().constructFromPrePost(preorder, postorder))
