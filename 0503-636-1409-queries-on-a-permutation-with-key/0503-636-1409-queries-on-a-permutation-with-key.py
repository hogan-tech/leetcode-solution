# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i + 1 for i in range(m)]
        result = []
        for query in queries:
            currIdx = P.index(query)
            result.append(currIdx)
            P = [P[currIdx]] + P[:currIdx] + P[currIdx + 1:]
        return result


queries = [3, 1, 2, 1]
m = 5
print(Solution().processQueries(queries, m))
queries = [4, 1, 2, 2]
m = 4
print(Solution().processQueries(queries, m))
queries = [7, 5, 5, 8, 3]
m = 8
print(Solution().processQueries(queries, m))
