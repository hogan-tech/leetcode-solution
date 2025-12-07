# time complexity: O(n)
# space complexity: O(n)
from typing import List
import bisect


class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        palindromeSet = set()

        for length in range(1, 14):
            halfLen = (length + 1) // 2
            start = 1 << (halfLen - 1)
            end = 1 << halfLen
            for half in range(start, end):
                s = bin(half)[2:]
                if length % 2 == 0:
                    pal = s + s[::-1]
                else:
                    pal = s + s[-2::-1]
                val = int(pal, 2)
                if val <= 5000:
                    palindromeSet.add(val)

        palindromeSet = sorted(palindromeSet)

        result = []
        for num in nums:
            pos = bisect.bisect_left(palindromeSet, num)

            best = float('inf')

            if pos < len(palindromeSet):
                best = min(best, abs(palindromeSet[pos] - num))
            if pos > 0:
                best = min(best, abs(palindromeSet[pos - 1] - num))

            result.append(best)

        return result


nums = [1, 2, 4]
print(Solution().minOperations(nums))
nums = [6, 7, 12]
print(Solution().minOperations(nums))
