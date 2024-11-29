class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                res.append('None')
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        ls = data.split(',')
        root = TreeNode(int(ls[0]))
        queue = deque([root])

        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            left_val, right_val = ls[i], ls[i+1] if i + 1 < len(ls) else 'None'

            if left_val != 'None':
                node.left = TreeNode(int(left_val))
                queue.append(node.left)

            if right_val != 'None':
                node.right = TreeNode(int(right_val))
                queue.append(node.right)

            i += 2

        return root