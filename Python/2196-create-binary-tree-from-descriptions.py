# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        self.traverse(node.left)
        print(node.val)
        self.traverse(node.right)

    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        nodeMap = {}
        children = set()
        for parent, child, isLeft in descriptions:
            if parent not in nodeMap:
                nodeMap[parent] = TreeNode(parent)
            if child not in nodeMap:
                nodeMap[child] = TreeNode(child)
            if isLeft:
                nodeMap[parent].left = nodeMap[child]
            else:
                nodeMap[parent].right = nodeMap[child]
            children.add(child)
        for node in nodeMap.values():
            if node.val not in children:
                self.traverse(node)
                return node
        return None


descriptions = [[20, 15, 1], [20, 17, 0],
                [50, 20, 1], [50, 80, 0], [80, 19, 1]]
print(Solution().createBinaryTree(descriptions))
