# time complextiy: O(n+q)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        maxHeightAfterRemoval = [0] * 100001
        self.currentMaxHeight = 0

        def traverseLeftToRight(node, currentHeight):
            if not node:
                return

            maxHeightAfterRemoval[node.val] = self.currentMaxHeight

            self.currentMaxHeight = max(
                self.currentMaxHeight, currentHeight
            )

            traverseLeftToRight(node.left, currentHeight + 1)
            traverseLeftToRight(node.right, currentHeight + 1)

        def traverseRightToLeft(node, currentHeight):
            if not node:
                return

            maxHeightAfterRemoval[node.val] = max(
                maxHeightAfterRemoval[node.val], self.currentMaxHeight
            )

            self.currentMaxHeight = max(
                currentHeight, self.currentMaxHeight
            )

            traverseRightToLeft(node.right, currentHeight + 1)
            traverseRightToLeft(node.left, currentHeight + 1)

        traverseLeftToRight(root, 0)
        self.currentMaxHeight = 0
        traverseRightToLeft(root, 0)

        return [maxHeightAfterRemoval[q] for q in queries]
