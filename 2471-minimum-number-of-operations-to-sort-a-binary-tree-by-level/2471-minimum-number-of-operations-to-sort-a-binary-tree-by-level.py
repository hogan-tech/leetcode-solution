from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        totalSwaps = 0
        while queue:
            levelSize = len(queue)
            levelValues = []
            for _ in range(levelSize):
                node = queue.popleft()
                levelValues.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            totalSwaps += self.getMinSwaps(levelValues)
        return totalSwaps

    def getMinSwaps(self, original: list) -> int:
        swaps = 0
        target = sorted(original)
        pos = {val: idx for idx, val in enumerate(original)}
        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1
                curPos = pos[target[i]]
                pos[original[i]] = curPos
                original[curPos] = original[i]
        return swaps


root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(6)
root.right.left = TreeNode(8)
root.right.left.left = TreeNode(5)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(10)
print(Solution().minimumOperations(root))
