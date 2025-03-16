# time complexity: O(nlogn)
# space complexity: O(n)
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        numIdxMap = defaultdict(list)
        for i, num in enumerate(nums):
            numIdxMap[num].append(i)
        result = []
        n = len(nums)

        for query in queries:
            currNum = nums[query]
            numIdxArr = numIdxMap[currNum]
            if len(numIdxArr) == 1:
                result.append(-1)
                continue

            targetIdx = bisect_left(numIdxArr, query)
            prevIdx = numIdxArr[targetIdx -
                                1] if targetIdx - 1 >= 0 else numIdxArr[-1]
            nextIdx = numIdxArr[targetIdx] if targetIdx < len(numIdxArr) and numIdxArr[targetIdx] != query \
                else (numIdxArr[(targetIdx + 1) % len(numIdxArr)] if len(numIdxArr) > 1 else None)

            minDis = float('inf')
            if prevIdx != query:
                dist1 = (query - prevIdx + n) % n
                dist2 = (prevIdx - query + n) % n
                minDis = min(minDis, dist1, dist2)

            if nextIdx != query:
                dist1 = (nextIdx - query + n) % n
                dist2 = (query - nextIdx + n) % n
                minDis = min(minDis, dist1, dist2)

            result.append(minDis if minDis != float('inf') else -1)
        return result


nums = [6, 12, 17, 9, 16, 7, 6]
queries = [5, 6, 0, 4]
print(Solution().solveQueries(nums, queries))
'''
0 1 2 3 4 5 6 7 8 | 9 10 11 12 13 14 15 16 17 18
V V         V   V   V  
'''
nums = [14, 14, 4, 2, 19, 19, 14, 19, 14]
queries = [2, 4, 8, 6, 3]
print(Solution().solveQueries(nums, queries))
'''
0 1 2 3 4 5 6 | 7 8 9 10 11 12 13 
  V       V       V          V
'''
nums = [1, 3, 1, 4, 1, 3, 2]
queries = [0, 3, 5]
print(Solution().solveQueries(nums, queries))
nums = [1, 2, 3, 4]
queries = [0, 1, 2, 3]
print(Solution().solveQueries(nums, queries))
