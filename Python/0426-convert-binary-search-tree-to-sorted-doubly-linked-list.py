# time complexity: O(n)
# space complexity: O(n)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def traverse(node):
            nonlocal last, first
            if node:
                traverse(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                traverse(node.right)

        if not root:
            return None

        first, last = None, None
        traverse(root)

        last.right = first
        first.left = last
        return first


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
print(Solution().treeToDoublyList(root))
