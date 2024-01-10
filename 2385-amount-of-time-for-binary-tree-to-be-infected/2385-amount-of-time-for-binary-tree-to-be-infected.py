# time complexity: O(n)
# space complexity: O(n)
# Definition for a binary tree node.
from collections import deque
from typing import Dict, Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertTreeToGraph(self, current: TreeNode, parent: int, treeMap: Dict[int, Set[int]]):
        if current is None:
            return
        if current.val not in treeMap:
            treeMap[current.val] = set()
        adjacentList = treeMap[current.val]
        if parent != 0:
            adjacentList.add(parent)
        if current.left:
            adjacentList.add(current.left.val)
        if current.right:
            adjacentList.add(current.right.val)
        self.convertTreeToGraph(current.left, current.val, treeMap)
        self.convertTreeToGraph(current.right, current.val, treeMap)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        treeMap: Dict[int, Set[int]] = {}
        self.convertTreeToGraph(root, 0, treeMap)
        print(treeMap)

        queue = deque([start])
        minute = 0
        visited = {start}
        while queue:
            levelSize = len(queue)
            while levelSize > 0:
                current = queue.popleft()
                for num in treeMap[current]:
                    if num not in visited:
                        visited.add(num)
                        queue.append(num)
                levelSize -= 1
            minute += 1
        return minute - 1


root = TreeNode(1)
root.left = TreeNode(5)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)

print(Solution().amountOfTime(root, 3))
