# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional



class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def traverse(left, right):
            nonlocal postorderIdx
            if left > right:
                return None
            rootVal = postorder[postorderIdx]
            root = TreeNode(rootVal)
            postorderIdx -= 1
            root.right = traverse(inorderMap[rootVal] + 1, right)
            root.left = traverse(left, inorderMap[rootVal] - 1)
            return root
        inorderMap = {}
        for i, val in enumerate(inorder):
            inorderMap[val] = i
        postorderIdx = len(postorder) - 1
        return traverse(0, len(inorder) - 1)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print(Solution().buildTree(inorder, postorder))
