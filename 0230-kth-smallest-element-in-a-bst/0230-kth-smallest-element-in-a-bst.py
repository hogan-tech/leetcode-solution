# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addToArr(self, node: Optional[TreeNode], treeList: List[int]) -> None:
        if node:
            self.addToArr(node.left, treeList)
            treeList.append(node.val)
            self.addToArr(node.right, treeList)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.addToArr(root, result)
        return result[k-1]