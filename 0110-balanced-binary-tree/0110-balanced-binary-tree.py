class Solution(object):
    def height(self, node):
        if node == None:
            return -1
        return 1+max(self.height(node.left), self.height(node.right))

    def isBalanced(self, node):
        if node == None:
            return True
        if abs(self.height(node.left) - self.height(node.right)) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)