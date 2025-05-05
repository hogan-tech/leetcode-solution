# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        hashSet = defaultdict(list)
        for value, label in zip(values, labels):
            heappush(hashSet[label], value)
            if len(hashSet[label]) > useLimit:
                heappop(hashSet[label])

        result = []
        for remainValues in hashSet.values():
            result.extend(remainValues)

        result.sort(reverse=True)
        return sum(result[:numWanted])


values = [5, 4, 3, 2, 1]
labels = [1, 1, 2, 2, 3]
numWanted = 3
useLimit = 1
print(Solution().largestValsFromLabels(values, labels, numWanted, useLimit))
values = [5, 4, 3, 2, 1]
labels = [1, 3, 3, 3, 2]
numWanted = 3
useLimit = 2
print(Solution().largestValsFromLabels(values, labels, numWanted, useLimit))
values = [9, 8, 8, 7, 6]
labels = [0, 0, 0, 1, 1]
numWanted = 3
useLimit = 1
print(Solution().largestValsFromLabels(values, labels, numWanted, useLimit))
values = [9, 8, 8, 7, 6]
lavels = [0, 0, 0, 1, 1]
numWanted = 3
useLimit = 2
print(Solution().largestValsFromLabels(values, labels, numWanted, useLimit))
