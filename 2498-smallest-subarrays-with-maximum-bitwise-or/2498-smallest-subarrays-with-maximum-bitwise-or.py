# time complexity: O(nlogc)
# space complexity: O(logc)
from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        position = [-1] * 31
        result = [0] * n
        for i in range(n - 1, -1, -1):
            j = i
            for bit in range(31):
                if (nums[i] & (1 << bit)) == 0:
                    if position[bit] != -1:
                        j = max(j, position[bit])
                else:
                    position[bit] = i
            result[i] = j - i + 1
        return result


nums = [1, 0, 2, 1, 3]
print(Solution().smallestSubarrays(nums))
nums = [1, 2]
print(Solution().smallestSubarrays(nums))
