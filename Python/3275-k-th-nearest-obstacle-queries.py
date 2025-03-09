# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        result = []
        queries = [abs(x) + abs(y) for x, y in queries]
        hp = []
        for i in range(len(queries)):
            heappush(hp, -queries[i])
            if len(hp) > k:
                heappop(hp)
            if len(hp) == k:
                result.append(-hp[0])
            else:
                result.append(-1)

        return result


queries = [[1, 2], [3, 4], [2, 3], [-3, 0]]
k = 2
'''
hp = -3
result = -1
hp = -3 -7
result = -1 -7
hp = -3 -5
'''
print(Solution().resultsArray(queries, k))
queries = [[5, 5], [4, 4], [3, 3]]
k = 1
print(Solution().resultsArray(queries, k))
