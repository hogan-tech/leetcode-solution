# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        distinctCount = defaultdict(int)
        totalCount = 0
        left = 0
        right = 0
        currCount = 0
        while right < len(nums):
            distinctCount[nums[right]] += 1
            if distinctCount[nums[right]] == 1:
                k -= 1
            if k < 0:
                distinctCount[nums[left]] -= 1
                if distinctCount[nums[left]] == 0:
                    k += 1
                left += 1
                currCount = 0
            if k == 0:
                while distinctCount[nums[left]] > 1:
                    distinctCount[nums[left]] -= 1
                    left += 1
                    currCount += 1
                totalCount += (currCount + 1)
            right += 1
        return totalCount


nums = [1, 2, 1, 2, 3]
k = 2
print(Solution().subarraysWithKDistinct(nums, k))
