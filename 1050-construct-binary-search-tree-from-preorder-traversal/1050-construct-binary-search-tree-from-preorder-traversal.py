# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional





class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(left: int, right: int):
            nonlocal preorderIdx
            if left > right:
                return None
            rootValue = preorder[preorderIdx]
            root = TreeNode(rootValue)
            preorderIdx += 1
            root.left = dfs(left, inorderMap[rootValue] - 1)
            root.right = dfs(inorderMap[rootValue] + 1, right)
            return root

        inorder = sorted(preorder)
        preorderIdx = 0
        inorderMap = {}

        for i, value in enumerate(inorder):
            inorderMap[value] = i

        return dfs(0, len(inorder) - 1)


preorder = [8, 5, 1, 7, 10, 12]
print(Solution().bstFromPreorder(preorder))
preorder = [1, 3]
print(Solution().bstFromPreorder(preorder))
