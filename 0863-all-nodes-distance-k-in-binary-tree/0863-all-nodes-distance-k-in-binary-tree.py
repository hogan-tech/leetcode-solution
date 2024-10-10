# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def buildGraph(curr: TreeNode, parent: TreeNode):
            if curr and parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            if curr.left:
                buildGraph(curr.left, curr)
            if curr.right:
                buildGraph(curr.right, curr)

        buildGraph(root, None)
        queue = deque()
        queue.append((target.val, 0))
        seen = set([target.val])
        result = []

        while queue:
            currNodeVal, distance = queue.popleft()
            if distance == k:
                result.append(currNodeVal)
            for neighbor in graph[currNodeVal]:
                if neighbor not in seen:
                    queue.append((neighbor, distance + 1))
                    seen.add(neighbor)


        return result


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
target = TreeNode(5)
k = 2
print(Solution().distanceK(root, target, k))
