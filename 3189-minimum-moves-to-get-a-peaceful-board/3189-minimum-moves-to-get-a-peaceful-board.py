# time complexity: O(nlogn)
# space complexxity: O(1)
from typing import List


class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        distance = 0
        rooks.sort()
        for i in range(len(rooks)):
            distance += abs(rooks[i][0] - i)
        rooks.sort(key=lambda x: x[1])
        for i in range(len(rooks)):
            distance += abs(rooks[i][1] - i)

        return distance


rooks = [[0, 0], [1, 3], [4, 1], [2, 4], [2, 0]]
print(Solution().minMoves(rooks))
