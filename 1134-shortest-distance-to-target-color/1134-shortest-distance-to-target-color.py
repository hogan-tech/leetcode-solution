# time complexity: O(qlogn + n)
# space complexity: O(n)
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        for i, c in enumerate(colors):
            hashmap[c].append(i)

        result = []
        for i, (target, color) in enumerate(queries):
            if color not in hashmap:
                result.append(-1)
                continue

            idxList = hashmap[color]
            insert = bisect_left(idxList, target)

            leftNearest = abs(idxList[max(insert - 1, 0)] - target)
            rightNearest = abs(idxList[min(insert, len(idxList) - 1)] - target)
            result.append(min(leftNearest, rightNearest))

        return result


colors = [1, 1, 2, 1, 3, 2, 2, 3, 3]
queries = [[1, 3], [2, 2], [6, 1]]
print(Solution().shortestDistanceColor(colors, queries))
colors = [1, 2]
queries = [[0, 3]]
print(Solution().shortestDistanceColor(colors, queries))
