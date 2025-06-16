# time complexity: O(n)
# space complexity: O(n)
from typing import List
from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        countRight = defaultdict(int)
        for num in nums:
            countRight[num] += 1

        countLeft = defaultdict(int)
        result = 0

        for j in range(len(nums)):
            mid = nums[j]
            countRight[mid] -= 1

            target = mid * 2
            result += countLeft[target] * countRight[target]
            result %= MOD

            countLeft[mid] += 1

        return result


nums = [6, 3, 6]
print(Solution().specialTriplets(nums))
nums = [0, 1, 0, 0]
print(Solution().specialTriplets(nums))
nums = [8, 4, 2, 8, 4]
print(Solution().specialTriplets(nums))
