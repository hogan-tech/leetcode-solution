# time complextiy: O(n+q)
# space complexity: O(n)
from collections import defaultdict
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


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        nodeDepth = {}
        nodeHeight = {}

        def dfs(node, depth, nodeDepth, nodeHeight):
            if not node:
                return -1
            nodeDepth[node.val] = depth
            height = max(dfs(node.left, depth + 1, nodeDepth, nodeHeight),
                         dfs(node.right, depth + 1, nodeDepth, nodeHeight)) + 1
            nodeHeight[node.val] = height
            return height

        dfs(root, 0, nodeDepth, nodeHeight)

        depthGroups = defaultdict(list)
        for value, depth in nodeDepth.items():
            depthGroups[depth].append((nodeHeight[value], value))
            depthGroups[depth].sort(reverse=True)
            if len(depthGroups[depth]) > 2:
                depthGroups[depth].pop()

        result = []

        for q in queries:
            depth = nodeDepth[q]
            if len(depthGroups[depth]) == 1:
                result.append(depth - 1)
            elif depthGroups[depth][0][1] == q:
                result.append(depthGroups[depth][1][0] + depth)
            else:
                result.append(depthGroups[depth][0][0] + depth)
        return result
