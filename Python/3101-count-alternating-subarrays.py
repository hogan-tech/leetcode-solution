# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        prev = nums[0]
        result = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count = 1
            else:
                count += 1
                prev = nums[i]
            result += count
        return result


nums = [0, 1, 1, 1]
print(Solution().countAlternatingSubarrays(nums))
nums = [1, 0, 1, 0]
print(Solution().countAlternatingSubarrays(nums))
'''
0 1 1 1
1 2 1 1

1 0 1 0
1 2 3 4

1 1 1
1 1 1

1 0 1 1
1 2 3 1
'''
