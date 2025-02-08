# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        result = 0
        nums.sort(reverse=True)
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix > 0:
                result += 1
        return result


nums = [2, -1, 0, 1, -3, 3, -3]
print(Solution().maxScore(nums))
nums = [-2, -3, 0]
print(Solution().maxScore(nums))
nums = [-687767, -860350, 950296, 52109, 510127, 545329, -291223, -966728, 852403, 828596,
        456730, -483632, -529386, 356766, 147293, 572374, 243605, 931468, 641668, 494446]
print(Solution().maxScore(nums))
