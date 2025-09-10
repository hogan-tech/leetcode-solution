# time complexity: O(n^3)
# space complexity: O(n)
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []
            if not nums:
                return result
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        result.append([nums[i]] + subset)
            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            left, right = 0, len(nums) - 1
            while (left < right):
                currSum = nums[left] + nums[right]
                if currSum < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                elif currSum > target or (right < len(nums)-1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return result
        
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            seen = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in seen and (not result or [complement, num] != result[-1]):
                    result.append([complement, num])
                seen[num] = i
            return result
        nums.sort()
        return kSum(nums, target, 4)
    
        


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))
nums = [2, 2, 2, 2, 2]
target = 8
print(Solution().fourSum(nums, target))
