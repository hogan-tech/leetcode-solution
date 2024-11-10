# time complexity: O(logn)
# space complexity: O(n)

from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        increasingLengths = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasingLengths[i] = increasingLengths[i - 1] + 1
            else:
                increasingLengths[i] = 1

        left, right = 1, n // 2
        maxK = 0

        while left <= right:
            mid = (left + right) // 2
            found = False

            i = 0
            while i + 2 * mid <= n:
                if increasingLengths[i + mid - 1] >= mid and increasingLengths[i + 2 * mid - 1] >= mid:
                    found = True
                    break
                i += 1

            if found:
                maxK = mid
                left = mid + 1
            else:
                right = mid - 1

        return maxK


solution = Solution()
print(solution.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
print(solution.maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
