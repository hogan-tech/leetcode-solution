# time complexity: O(n log n)
# space complexity: O(n)
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        halfTotal = sum(nums) / 2
        currTotal = sum(nums)
        hp = [-num for num in nums]
        heapify(hp)
        count = 0
        while currTotal > halfTotal:
            biggestNum = -heappop(hp)
            halfNum = biggestNum / 2
            currTotal -= halfNum
            heappush(hp, -halfNum)
            count += 1
        return count


nums = [5, 19, 8, 1]
print(Solution().halveArray(nums))
nums = [3, 8, 20]
print(Solution().halveArray(nums))
