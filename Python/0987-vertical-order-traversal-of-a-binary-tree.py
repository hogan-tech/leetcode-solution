# time complexity: O(n)
# space complexity: O(n)
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodeList = []

        def DFS(node, row, column):
            if node is not None:
                nodeList.append((column, row, node.val))
                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        nodeList.sort()

        ret = []
        currColumnIndex = nodeList[0][0]
        currColumn = []
        for column, row, value in nodeList:
            if column == currColumnIndex:
                currColumn.append(value)
            else:
                ret.append(currColumn)
                currColumnIndex = column
                currColumn = [value]
        ret.append(currColumn)

        return ret


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().verticalTraversal(root))
