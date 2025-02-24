# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        candleList = []
        for i, c in enumerate(s):
            if c == '|':
                candleList.append(i)

        result = []
        for leftQuery, rightQuery in queries:
            leftPlateIdx = binarySearch(candleList, leftQuery)
            rightPlateIdx = binarySearch(candleList, rightQuery + 1) - 1
            if leftPlateIdx < rightPlateIdx:
                plateCount = rightPlateIdx - leftPlateIdx
                plateAndCandles = candleList[rightPlateIdx] - candleList[leftPlateIdx]
                candleCount = plateAndCandles - plateCount
                result.append(candleCount)
            else:
                result.append(0)

        return result


s = "**|**|***|"
queries = [[2, 5], [5, 9]]
print(Solution().platesBetweenCandles(s, queries))
s = "***|**|*****|**||**|*"
queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
print(Solution().platesBetweenCandles(s, queries))
s = "||*"
queries = [[2, 2]]
print(Solution().platesBetweenCandles(s, queries))
