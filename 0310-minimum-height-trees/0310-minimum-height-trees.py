from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        neighbors: List[set] = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(leaves)
            newLeaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves