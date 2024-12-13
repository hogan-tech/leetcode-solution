# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))

        result = 0
        while heap:
            currNum, currIdx = heappop(heap)
            if not visited[currIdx]:
                result += currNum
                visited[currIdx] = True
                if currIdx - 1 >= 0:
                    visited[currIdx - 1] = True
                if currIdx + 1 < len(nums):
                    visited[currIdx + 1] = True

        return result


nums = [2, 1, 3, 4, 5, 2]
print(Solution().findScore(nums))
nums = [2, 3, 5, 1, 3, 2]
print(Solution().findScore(nums))
