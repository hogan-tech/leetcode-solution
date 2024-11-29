# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import defaultdict
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = defaultdict(list)
        for child in range(1, n):
            tree[parent[child]].append(child)
        lastSeen = {}
        newParent = parent[:]

        def dfs(node):
            char = s[node]
            if char in lastSeen:
                ancestor = lastSeen[char]
                if parent[node] != ancestor:
                    newParent[node] = ancestor

            previousAncestor = lastSeen.get(char)
            lastSeen[char] = node

            for child in tree[node]:
                dfs(child)

            if previousAncestor is not None:
                lastSeen[char] = previousAncestor
            else:
                del lastSeen[char]

        dfs(0)

        new_tree = defaultdict(list)
        for child in range(1, n):
            new_tree[newParent[child]].append(child)
        answer = [0] * n

        def calculateSizes(node):
            size = 1
            for child in new_tree[node]:
                size += calculateSizes(child)
            answer[node] = size
            return size
        calculateSizes(0)

        return answer


parent = [-1, 0, 0, 1, 1, 1]
s = "abaabc"
print(Solution().findSubtreeSizes(parent, s))
parent = [-1, 0, 4, 0, 1]
s = "abbba"
print(Solution().findSubtreeSizes(parent, s))
