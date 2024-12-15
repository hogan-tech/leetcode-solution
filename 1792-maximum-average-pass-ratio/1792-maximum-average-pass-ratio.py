# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculate(passAmount: int, total: int) -> float:
            return (passAmount+1) / (total+1) - passAmount/total

        maxHeap = []
        for currPass, currTotal in classes:
            gain = calculate(currPass, currTotal)
            heappush(maxHeap, (-gain, currPass, currTotal))

        for _ in range(extraStudents):
            _, currPass, currTotal = heappop(maxHeap)
            heappush(maxHeap, (-calculate(currPass + 1, currTotal + 1),
                     currPass + 1, currTotal + 1))

        result = 0
        for _, currPass, currTotal in maxHeap:
            result += (currPass / currTotal)
        return result / len(maxHeap)


classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(Solution().maxAverageRatio(classes, extraStudents))
classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
print(Solution().maxAverageRatio(classes, extraStudents))
