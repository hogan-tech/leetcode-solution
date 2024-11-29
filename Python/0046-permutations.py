from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i, item in enumerate(list(permutations(nums))):
            result.append(list(item))
        return result

        # out = []
        # stack = [[]]
        # while stack:
        #     curr = stack.pop()
        #     if len(curr) == len(nums):
        #         out.append(curr)
        #         continue
        #     for num in nums:
        #         if num not in curr:
        #             stack.append((curr + [num]))
        #     print(out)
        # return []