# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]):
        ans = []
        for num in nums:
            found = False
            for item in range(num):
                if item | (item + 1) == num:
                    ans.append(item)
                    found = True
                    break
            if not found:
                ans.append(-1)

        return ans


nums = [11, 13, 31]
print(Solution().minBitwiseArray(nums))
