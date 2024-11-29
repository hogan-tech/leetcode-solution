from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        newNums = sorted(set(nums))
        j = 0
        for i in range(len(newNums)):
            while j < len(newNums) and newNums[j] < newNums[i] + n:
                j += 1
            count = j - i
            ans = min(ans, n - count)
        return ans


nums = [4,2,5,6]
print(Solution().minOperations(nums))