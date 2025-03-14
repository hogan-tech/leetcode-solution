# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticalMap = defaultdict(list)
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, col = queue.popleft()
            verticalMap[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        result = []

        for key in sorted(verticalMap.keys()):
            result.append(verticalMap[key])

        return result


root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(Solution().verticalOrder(root1))
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(10)
root2.right.left = TreeNode(9)
root2.right.right = TreeNode(11)
root2.left.left.right = TreeNode(5)
root2.left.left.right.right = TreeNode(6)
print(Solution().verticalOrder(root2))
