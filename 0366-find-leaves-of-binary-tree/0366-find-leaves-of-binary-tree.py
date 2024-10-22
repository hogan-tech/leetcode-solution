# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heightDict = defaultdict(list)

        def getHeight(node):
            if not node:
                return -1
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            currHeight = max(leftHeight, rightHeight) + 1
            heightDict[currHeight].append(node.val)

            return currHeight

        getHeight(root)
        result = []
        for value in heightDict.values():
            result.append(value)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().findLeaves(root))
