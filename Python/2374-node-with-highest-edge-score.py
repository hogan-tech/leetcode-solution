# time complexity: O(n)
# sapce complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scoreMap = defaultdict(int)
        for i, edge in enumerate(edges):
            scoreMap[edge] += i

        maxScore = float('-inf')
        result = 0
        for key, value in scoreMap.items():
            if value > maxScore:
                maxScore = value
                result = key
            if value == maxScore and key < result:
                result = key
        return result


edges = [1, 0, 0, 0, 0, 7, 7, 5]
print(Solution().edgeScore(edges))
edges = [2, 0, 0, 2]
print(Solution().edgeScore(edges))
edges = [2, 0, 0, 1]
print(Solution().edgeScore(edges))
