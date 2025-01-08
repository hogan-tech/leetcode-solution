# time complexity: O(n)
# space complexity: O(h)
from collections import deque
from typing import Optional




class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                result.append('None')
        
        return ','.join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        dataList = data.split(',')
        root = TreeNode(int(dataList[0]))
        queue = deque([root])

        i = 1
        while queue and i < len(dataList):
            node = queue.popleft()
            leftVal, rightVal = dataList[i], dataList[i+1] if i + 1 < len(dataList) else 'None'

            if leftVal != 'None':
                node.left = TreeNode(int(leftVal))
                queue.append(node.left)

            if rightVal != 'None':
                node.right = TreeNode(int(rightVal))
                queue.append(node.right)

            i += 2

        return root


# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

ser = Codec()
deser = Codec()

tree = ser.serialize(root)
print(tree)  # '1,2,5,3,4,None,None,None,None,None,None,'

ans = deser.deserialize(tree)
print(ans.val)  # 1
print(ans.left.val)  # 2
print(ans.right.val)  # 5
print(ans.left.left.val)  # 3
print(ans.left.right.val)  # 4
