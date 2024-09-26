from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nodeList = []
        self.idx = 0
        self.traverse(self.root)

    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return
        self.traverse(node.left)
        self.nodeList.append(node.val)
        self.traverse(node.right)

    def next(self) -> int:
        self.idx += 1
        return self.nodeList[self.idx - 1]

    def hasNext(self) -> bool:
        if self.idx > len(self.nodeList) - 1:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

obj = BSTIterator(root)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
