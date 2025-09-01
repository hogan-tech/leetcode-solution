# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        prefix = 0
        for num in nums:
            prefix += num
            prefix = max(prefix, num)
            result = max(result, prefix)
        return result

# time complexity: O(nlogn)
# space complexity: O(logn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            if left > right:
                return float('-inf')

            mid = (left + right) // 2
            curr = bestLeftSum = bestRightSum = 0

            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                bestLeftSum = max(bestLeftSum, curr)

            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                bestRightSum = max(bestRightSum, curr)

            bestCombinedSum = nums[mid] + bestLeftSum + bestRightSum

            leftHalf = findBestSubarray(nums, left, mid - 1)
            rightHalf = findBestSubarray(nums, mid + 1, right)

            return max(bestCombinedSum, leftHalf, rightHalf)

        return findBestSubarray(nums, 0, len(nums) - 1)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
nums = [1]
print(Solution().maxSubArray(nums))
nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))
