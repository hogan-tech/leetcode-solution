# time complexity: O((k+m)*logm)
# space complexity: O(m)
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))

        heapify(pq)
        answer = 0
        nextHead, nextTail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            curCost, curSectionId = heappop(pq)
            answer += curCost
            if nextHead <= nextTail:
                if curSectionId == 0:
                    heappush(pq, (costs[nextHead], 0))
                    nextHead += 1
                else:
                    heappush(pq, (costs[nextTail], 1))
                    nextTail -= 1
        return answer


costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
print(Solution().totalCost(costs, k, candidates))
