# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def largestTimeFromDigits(self, nums: List[int]) -> str:
        result = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                hr = comb[0] * 10 + comb[1]
                min = comb[2] * 10 + comb[3]
                if 0 <= hr < 24 and 0 <= min < 60:
                    hr = "{:02d}".format(hr)
                    min = "{:02d}".format(min)
                    result.append(f"{hr}:{min}")
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))
        result.sort()
        return result[-1] if result else ""


arr = [1, 2, 3, 4]
print(Solution().largestTimeFromDigits(arr))
arr = [0, 0, 1, 0]
print(Solution().largestTimeFromDigits(arr))
arr = [5, 5, 5, 5]
print(Solution().largestTimeFromDigits(arr))
