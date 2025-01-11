# time complexity: O(n + nlogn)
# space complexity: O(n)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scoreDict = defaultdict(list)
        for id, score in items:
            heappush(scoreDict[id], score)
            if len(scoreDict[id]) > 5:
                heappop(scoreDict[id])
        result = []
        for id, values in sorted(scoreDict.items()):
            result.append([id, sum(values) // len(values)])

        return result


items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
    2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(Solution().highFive(items))
items = [[1, 100], [7, 100], [1, 100], [7, 100], [1, 100],
         [7, 100], [1, 100], [7, 100], [1, 100], [7, 100]]
print(Solution().highFive(items))
