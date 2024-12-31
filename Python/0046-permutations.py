# time complexity: O(n*n!)
# space complexity: O(n)
from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr: List[int]):
            if len(curr) == len(nums):
                result.append(curr[:])
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        result = []
        backtrack([])
        return result


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for _, item in enumerate(list(permutations(nums))):
#             result.append(list(item))
#         return result

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         out = []
#         stack = [[]]
#         while stack:
#             curr = stack.pop()
#             if len(curr) == len(nums):
#                 out.append(curr)
#                 continue
#             for num in nums:
#                 if num not in curr:
#                     stack.append((curr + [num]))
#             print(out)
#         return []


nums = [1, 2, 3]
print(Solution().permute(nums))
