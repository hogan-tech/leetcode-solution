# time complexity: O(e*k)
# space complexity: O(n)
from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            start, end, price = flight
            adj[start].append((end, price))

        priceList = [float('inf') for _ in range(n)]

        priceList[src] = 0
        queue = deque()
        queue.append((src, 0))
        stops = 0

        while queue and stops <= k:
            size = len(queue)
            for _ in range(size):
                currNode, currPrice = queue.popleft()
                for nextNode, nextPrice in adj[currNode]:
                    if currPrice + nextPrice < priceList[nextNode]:
                        priceList[nextNode] = currPrice + nextPrice
                        queue.append((nextNode, currPrice + nextPrice))
            stops += 1
        
        return priceList[dst] if priceList[dst] != float('inf') else -1

        

# Bellman Ford
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#         dist_price = [float('inf') for _ in range(n)]
#         dist_price[src]=0
#         for source,dest,cost in flights:
#             if src==source:
#                 dist_price[dest] = cost
#         for times in range(0,K):
#             temp = [*dist_price]
#             for srce,dest,cost in flights:
#                 temp[dest] = min(temp[dest] , cost + dist_price[srce])
#             dist_price = temp
#         if dist_price[dst] == float('inf'):
#             return -1
#         return dist_price[dst]

n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

print(Solution().findCheapestPrice(n, flights, src, dst, k))
