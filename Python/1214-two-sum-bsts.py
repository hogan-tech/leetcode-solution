# time complexity: O(m+n)
# space complexity: O(m+n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def traverse(node, nodeSet):
            if not node:
                return
            traverse(node.left, nodeSet)
            nodeSet.add(node.val)
            traverse(node.right, nodeSet)

        nodeSet1 = set()
        nodeSet2 = set()
        traverse(root1, nodeSet1)
        traverse(root2, nodeSet2)
        for value in nodeSet1:
            if target - value in nodeSet2:
                return True
        return False


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)
target = 5
print(Solution().twoSumBSTs(root1, root2, target))
