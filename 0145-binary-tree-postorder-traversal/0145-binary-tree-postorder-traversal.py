# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if not node:
                return
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            result.append(node.val)
        traverse(root)
        return result