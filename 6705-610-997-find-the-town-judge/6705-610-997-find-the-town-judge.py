# time complexity: O(e)
# space complexity: O(n)
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        inDegree = [0] * (n + 1)
        outDegree = [0] * (n + 1)
        for outNode, inNode in trust:
            outDegree[outNode] += 1
            inDegree[inNode] += 1
        for i in range(1, n + 1):
            if inDegree[i] == n - 1 and outDegree[i] == 0:
                return i
        return -1


n = 2
trust = [[1, 2]]
print(Solution().findJudge(n, trust))
n = 3
trust = [[1, 3], [2, 3]]
print(Solution().findJudge(n, trust))
n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(Solution().findJudge(n, trust))
