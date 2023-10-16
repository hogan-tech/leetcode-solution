from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        oddsResult = []
        for i in range(len(nums)):
            if nums[i] % 2:
                oddsResult.append(nums[i])
            else:
                result.append(nums[i])
        result += oddsResult
        return result


nums = [0]
print(Solution().sortArrayByParity(nums))