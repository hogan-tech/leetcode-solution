# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def twoSumII(self, i: int, nums: List[int], result: List[List[int]]):
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    def twoSumI(self, nums: List[int], left: int, result: List[List[int]]):
        numSet = set()
        right = left + 1
        while right < len(nums):
            complement = -nums[left] - nums[right]
            if complement in numSet:
                result.append([nums[left], nums[right], complement])
                while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                    right += 1
            numSet.add(nums[right])
            right += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, item in enumerate(nums):
            if item > 0:
                break
            if item != nums[i-1] or i == 0:
                self.twoSumII(i, nums, result)
        return result

# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, dups = set(), set()
        numMap = {}
        for i, num1 in enumerate(nums):
            if num1 not in dups:
                dups.add(num1)
                for j, num2 in enumerate(nums[i + 1 :]):
                    complement = -num1 - num2
                    if complement in numMap and numMap[complement] == i:
                        result.add(tuple(sorted((num1, num2, complement))))
                    numMap[num2] = i
        return [list(x) for x in result]
    
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
nums = [0, 1, 1]
print(Solution().threeSum(nums))
nums = [0, 0, 0]
print(Solution().threeSum(nums))
