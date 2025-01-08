# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(left: int, right: int):
            nonlocal preorderIndex
            if left > right:
                return None
            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue)
            preorderIndex += 1
            root.left = dfs(left, inorderMap[rootValue] - 1)
            root.right = dfs(inorderMap[rootValue] + 1, right)
            return root
        
        preorderIndex = 0
        inorderMap = {}
        for i, value in enumerate(inorder):
            inorderMap[value] = i

        return dfs(0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder))
