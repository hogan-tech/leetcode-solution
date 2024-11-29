from typing import List

# brute force
# time complexity: O(n^2)
# space complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

# hashMap
# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        return []


# two pointer
# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
   def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
       res = []
       left, right = 0, len(nums) - 1
       while (left < right):
           currSum = nums[left] + nums[right]
           if currSum < target or (left > 0 and nums[left] == nums[left - 1]):
               left += 1
           elif currSum > target or (right < len(nums)-1 and nums[right] == nums[right + 1]):
               right -= 1
           else:
               res.append([nums[left], nums[right]])
               left += 1
               right -= 1
       return res


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)

print(result)
