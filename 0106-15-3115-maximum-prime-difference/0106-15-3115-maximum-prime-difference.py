from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(num):
            if num == 0 or num == 1:
                return 0
            for i in range(2, num):
                if (num % i) == 0:
                    return 0
            return 1
        prime = [isPrime(num) for num in nums]
        left = 0
        right = 0
        for i in range(len(prime)):
            if prime[i]:
                left = i
                break
        for i in range(len(prime) - 1, -1, -1):
            if prime[i]:
                right = i
                break
                
        return right - left


nums = [4, 2, 9, 5, 3]
print(Solution().maximumPrimeDifference(nums))
nums = [4, 8, 2, 8]
print(Solution().maximumPrimeDifference(nums))
