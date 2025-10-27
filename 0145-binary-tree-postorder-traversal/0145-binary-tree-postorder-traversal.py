# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if node is None:
                return
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            result.append(node.val)
            return 
        traverse(root)
        return result
        