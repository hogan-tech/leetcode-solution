# time complexity: O(n*2^n)
# space complexity: O(n*2^n)
from itertools import chain, combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list(chain.from_iterable(combinations(nums, r)
                      for r in range(len(nums)+1)))
        for i, item in enumerate(result):
            result[i] = list(item)
        return result

# class Solution:
#    def subsets(self, nums: List[int]) -> List[List[int]]:
#        output = [[]]

#        for num in nums:
#            output += [curr + [num] for curr in output]

#        return output


nums = [1, 2, 3]

print(Solution().subsets(nums))
