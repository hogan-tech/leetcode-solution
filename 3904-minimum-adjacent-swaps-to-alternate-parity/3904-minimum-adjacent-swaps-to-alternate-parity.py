# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        evenCount = 0
        oddCount = 0
        evenOdd = []
        n = len(nums)
        for num in nums:
            evenOdd.append(num % 2)
            if num % 2:
                oddCount += 1
            else:
                evenCount += 1

        if abs(evenCount - oddCount) > 1:
            return -1

        def countSwaps(startEven: bool) -> int:
            swaps = 0
            target = 0 if startEven else 1
            pos = 0
            for i in range(n):
                if evenOdd[i] == target:
                    swaps += abs(i - pos)
                    pos += 2
            return swaps

        if evenCount > oddCount:
            return countSwaps(True)
        elif oddCount > evenCount:
            return countSwaps(False)
        else:
            return min(countSwaps(True), countSwaps(False))


nums = [2, 4, 6, 5, 7]
print(Solution().minSwaps(nums))
nums = [2, 4, 5, 7]
print(Solution().minSwaps(nums))
nums = [1, 2, 3]
print(Solution().minSwaps(nums))
nums = [4, 5, 6, 8]
print(Solution().minSwaps(nums))
