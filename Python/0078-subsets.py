# time complexity: O(n*2^n)
# space complexity: O(n)
from itertools import chain, combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, comb: List[int]):
            result.append(list(comb))
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(0, [])
        return result

# time complexity: O(n*2^n)
# space complexity: O(n*2^n)
class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            newSubsets = []
            for curr in result:
                temp = curr.copy()
                temp.append(num)
                newSubsets.append(temp)
            for curr in newSubsets:
                result.append(curr)
        return result

# time complexity: O(n*2^n)
# space complexity: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        for i in range(2**n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # append subset corresponding to that bitmask
            result.append([nums[j] for j in range(n) if bitmask[j] == "1"])

        return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list(chain.from_iterable(combinations(nums, r)
                      for r in range(len(nums)+1)))
        for i, item in enumerate(result):
            result[i] = list(item)
        return result


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output


nums = [1, 2, 3]
print(Solution().subsets(nums))
nums = [0]
print(Solution().subsets(nums))
