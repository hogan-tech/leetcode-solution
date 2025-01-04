
from typing import List

# time complexity: O(nlogsum)
# space complexity: O(1)
# Binary Search


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7

        def countAndSum(nums: List[int], n: int, target: int):
            count = 0
            currentSum = 0
            totalSum = 0
            windowSum = 0
            i = 0
            for j in range(n):
                currentSum += nums[j]
                windowSum += nums[j] * (j - i + 1)
                while currentSum > target:
                    windowSum -= currentSum
                    currentSum -= nums[i]
                    i += 1
                count += j - i + 1
                totalSum += windowSum
            return count, totalSum

        def sumOfFirstK(nums: List[int], n: int, k: int):
            minSum = min(nums)
            maxSum = sum(nums)
            left = minSum
            right = maxSum

            while left <= right:
                mid = left + (right - left) // 2
                if countAndSum(nums, n, mid)[0] >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            count, totalSum = countAndSum(nums, n, left)
            return totalSum - left * (count - k)

        result = (
            sumOfFirstK(nums, n, right) - sumOfFirstK(nums, n, left - 1)
        ) % mod
        return (result + mod) % mod

# time complexity: O(n^2*logn)
# space complexity: O(n^2)
# Brute Force


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        sumList = []
        for i in range(len(nums)):
            tempSum = 0
            for j in range(i, len(nums)):
                tempSum += nums[j]
                sumList.append(tempSum)
        sumList.sort()
        result = 0
        for i in range(left-1, right):
            result += sumList[i]
            result %= MOD
        return result


nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
print(Solution().rangeSum(nums, n, left, right))

nums = [1, 2, 3, 4]
n = 4
left = 3
right = 4
print(Solution().rangeSum(nums, n, left, right))

nums = [1, 2, 3, 4]
n = 4
left = 1
right = 10
print(Solution().rangeSum(nums, n, left, right))
