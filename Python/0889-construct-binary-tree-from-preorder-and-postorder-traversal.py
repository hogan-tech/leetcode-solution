# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional





class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def traverse():
            nonlocal preIdx, postIdx
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            if root.val != postorder[postIdx]:
                root.left = traverse()
            if root.val != postorder[postIdx]:
                root.right = traverse()
            postIdx += 1
            return root
        preIdx = 0
        postIdx = 0
        return traverse()


preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
print(Solution().constructFromPrePost(preorder, postorder))
