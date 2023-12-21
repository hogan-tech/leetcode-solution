from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = deque([[root, None]])

        while queue:
            n = len(queue)

            visited = set()

            for _ in range(n):
                node, parent = queue.popleft()

                if node.right in visited:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root

                visited.add(node)

                if node.right:
                    queue.append([node.right, node])
                if node.left:
                    queue.append([node.left, node])
