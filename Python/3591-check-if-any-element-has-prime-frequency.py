# time complexity: O(nlogn)
# space complexity: O(1)
from typing import Counter, List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def checkprime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True
        for count in Counter(nums).values():
            if checkprime(count):
                return True

        return False


nums = [1, 2, 3, 4, 5, 4]
print(Solution().checkPrimeFrequency(nums))
nums = [1, 2, 3, 4, 5]
print(Solution().checkPrimeFrequency(nums))
nums = [2, 2, 2, 4, 4]
print(Solution().checkPrimeFrequency(nums))
