from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        patternList = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                patternList.append(0)
            elif nums[i] > nums[i - 1]:
                patternList.append(1)
            else:
                patternList.append(-1)

        count = 0
        for i in range(len(patternList) - len(pattern) + 1):
            if patternList[i: i + len(pattern)] == pattern:
                count += 1
        return count


nums = [1, 2, 3, 4, 5, 6]
pattern = [1, 1]
print(Solution().countMatchingSubarrays(nums, pattern))
nums = [1, 4, 4, 1, 3, 5, 5, 3]
pattern = [1, 0, -1]
print(Solution().countMatchingSubarrays(nums, pattern))
