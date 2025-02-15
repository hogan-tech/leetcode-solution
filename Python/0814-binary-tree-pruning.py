from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def containOne(node):
            if not node:
                return False
            leftContainOne = containOne(node.left)
            rightContainOne = containOne(node.right)
            if not leftContainOne:
                node.left = None
            if not rightContainOne:
                node.right = None
            
            return node.val or containOne(node.left) or containOne(node.right)

        return root if containOne(root) else None


root = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
print(Solution().pruneTree(root))
