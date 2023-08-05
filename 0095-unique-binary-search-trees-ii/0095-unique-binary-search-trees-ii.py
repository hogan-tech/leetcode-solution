# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossobleBST(self, start, end, memo):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[(start, end)]

        for i in range(start, end+1):
            leftSubTree = self.allPossobleBST(start, i - 1, memo)
            rightSubTree = self.allPossobleBST(i + 1, end, memo)
            for left in leftSubTree:
                for right in rightSubTree:
                    root = TreeNode(i, left, right)
                    res.append(root)

        memo[(start, end)] = res
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.allPossobleBST(1, n, memo)
