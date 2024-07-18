# time complexity: O(n^2)
# space complexity: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, currNode: TreeNode, prevNode: TreeNode, graph: set, leafNodes: set):
        if currNode is None:
            return
        if currNode.left is None and currNode.right is None:
            leafNodes.add(currNode)
        if prevNode is not None:
            if prevNode not in graph:
                graph[prevNode] = []
            graph[prevNode].append(currNode)

            if currNode not in graph:
                graph[currNode] = []
            graph[currNode].append(prevNode)

        self.traverseTree(currNode.left, currNode, graph, leafNodes)
        self.traverseTree(currNode.right, currNode, graph, leafNodes)

    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = {}
        leafNodes = set()

        self.traverseTree(root, None, graph, leafNodes)

        ans = 0

        for leaf in leafNodes:
            bfsQueue = []
            seen = set()
            bfsQueue.append(leaf)
            seen.add(leaf)
            for i in range(distance + 1):
                size = len(bfsQueue)
                for j in range(size):
                    currNode = bfsQueue.pop(0)
                    if currNode in leafNodes and currNode != leaf:
                        ans += 1
                    if currNode in graph:
                        for neighbor in graph.get(currNode):
                            if neighbor not in seen:
                                bfsQueue.append(neighbor)
                                seen.add(neighbor)
        return ans // 2


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
distance = 3
print(Solution().countPairs(root, distance))
