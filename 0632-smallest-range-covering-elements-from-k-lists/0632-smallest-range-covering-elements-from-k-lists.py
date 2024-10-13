# time complexity: O(nlogk)
# space complexity: O(k)
import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        maxVal = float("-inf")
        rangeStart = 0
        rangeEnd = float("inf")

        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0], i, 0))
            maxVal = max(maxVal, nums[i][0])

        while len(pq) == len(nums):
            minVal, currRow, currCol = heapq.heappop(pq)

            if maxVal - minVal < rangeEnd - rangeStart:
                rangeEnd = maxVal
                rangeStart = minVal

            if currCol + 1 < len(nums[currRow]):
                nextVal = nums[currRow][currCol + 1]
                heapq.heappush(pq, (nextVal, currRow, currCol + 1))
                maxVal = max(maxVal, nextVal)

        return [rangeStart, rangeEnd]


nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print(Solution().smallestRange(nums))
