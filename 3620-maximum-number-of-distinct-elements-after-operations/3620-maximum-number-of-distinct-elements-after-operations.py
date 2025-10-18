# time complexity: O(nlogn)
# space complexity: O(logn)
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        count = 0
        prev = float('-inf')
        for num in nums:
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                count += 1
                prev = curr
        return count


nums = [1, 2, 2, 3, 3, 4]
k = 2
print(Solution().maxDistinctElements(nums, k))
nums = [4, 4, 4, 4]
k = 1
print(Solution().maxDistinctElements(nums, k))
