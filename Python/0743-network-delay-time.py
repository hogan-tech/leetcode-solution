# time complexity: O(n + elogn)
# space complexity: O(n+e)
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = set()
        nodeMap = defaultdict(list)
        for source, dest, time in times:
            nodeMap[source].append((dest, time))

        minHeap = [(0, k)]
        print(minHeap)
        heapq.heapify(minHeap)
        while minHeap:
            currentTime, node = heapq.heappop(minHeap)
            seen.add(node)
            if len(seen) == n:
                return currentTime
            for neighbor, time in nodeMap[node]:
                if neighbor not in seen:
                    heapq.heappush(minHeap, (currentTime + time, neighbor))
        return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))
