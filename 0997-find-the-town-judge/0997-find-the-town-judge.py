# time complexity: O(e)
# space complexity: O(n)
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1
        inDegree = [0] * (N + 1)
        outDegree = [0] * (N + 1)
        for a, b in trust:
            outDegree[a] += 1
            inDegree[b] += 1
        for i in range(1, N + 1):
            if inDegree[i] == N - 1 and outDegree[i] == 0:
                return i
        return -1


n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(Solution().findJudge(n, trust))
