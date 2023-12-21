#time complexity: O(n+m *(v+elogv))
#space complexity: O(e+v+n)
from typing import List
from heapq import heappop, heappush
from math import inf


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjList = [[] for _ in range(n)]
        for fromNode, toNode, cost in edges:
            self.adjList[fromNode].append((toNode, cost))

    def addEdge(self, edge: List[int]) -> None:
        fromNode, toNode, cost = edge
        self.adjList[fromNode].append((toNode, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adjList)
        pq = [(0, node1)]
        costForNode = [inf] * (n)
        costForNode[node1] = 0

        while pq:
            currCost, currNode = heappop(pq)
            if currCost > costForNode[currNode]:
                continue
            if currNode == node2:
                return currCost
            for neighbor, cost in self.adjList[currNode]:
                newCost = currCost + cost
                if newCost < costForNode[neighbor]:
                    costForNode[neighbor] = newCost
                    heappush(pq, (newCost, neighbor))
        return -1
