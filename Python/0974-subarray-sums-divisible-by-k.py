# time complexity: O(n)
# space complexity: O(k)
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        prefixSum = 0
        count = 0
        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            if remainder < 0:
                remainder += k
            if remainder in map:
                count += map[remainder]
                map[remainder] += 1
            else:
                map[remainder] = 1
        return count


nums = [4, 5, 0, -2, -3, 1]
k = 5
print(Solution().subarraysDivByK(nums, k))
