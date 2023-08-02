# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = array_to_tree(left, inorder_map[root_value] - 1)
            root.right = array_to_tree(inorder_map[root_value] + 1, right)
            return root

        preorder_index = 0
        inorder_map = {}
        for index, value in enumerate(inorder):
            inorder_map[value] = index

        return array_to_tree(0, len(inorder) - 1)