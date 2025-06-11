# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def traverse(left: int, right: int):
            nonlocal preorderIdx
            if left > right:
                return None
            rootVal = preorder[preorderIdx]
            root = TreeNode(rootVal)
            preorderIdx += 1
            root.left = traverse(left, inorderMap[rootVal] - 1)
            root.right = traverse(inorderMap[rootVal] + 1, right)
            return root

        inorderMap = {val: i for i, val in enumerate(inorder)}
        preorderIdx = 0
        return traverse(0, len(preorder) - 1)


'''
        root
          |
preorder: 3 9 1 2 20 15 7
inorder : 1 9 2 3 15 20 7
                |

          l.  r.  l.    r
'''
