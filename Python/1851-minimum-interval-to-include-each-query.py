# time complexity: O(nlogn + qlogq)
# space complexity: O(n + q)
from heapq import heappop, heappush
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [0 for _ in range(len(queries))]
        intervals.sort(reverse=True)
        queriesIdx = sorted([(q, i) for i, q in enumerate(queries)])
        hp = []
        for query, i in queriesIdx:
            while len(intervals) and query >= intervals[-1][0]:
                start, end = intervals.pop()
                heappush(hp, [end - start + 1, end])
            while len(hp) and hp[0][1] < query:
                heappop(hp)
            if len(hp) == 0:
                result[i] = -1
            else:
                result[i] = hp[0][0]
        return result


intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
print(Solution().minInterval(intervals, queries))
intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
queries = [2, 19, 5, 22]
print(Solution().minInterval(intervals, queries))
