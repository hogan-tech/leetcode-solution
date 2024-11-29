# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inLeft: int, inRight: int) -> TreeNode:
            if inLeft > inRight:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idxMap[val]
            root.right = helper(index + 1, inRight)
            root.left = helper(inLeft, index - 1)
            return root
        idxMap = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print(Solution().buildTree(inorder, postorder))
