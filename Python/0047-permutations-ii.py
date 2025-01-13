# time complexity: O(sigma*P(n,k))
# space complexity: O(n)
from collections import Counter
from itertools import permutations
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        for _, item in enumerate(list(permutations(nums))):
            temp = list(item)
            if temp not in result:
                result.append(temp)
        return result


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))
