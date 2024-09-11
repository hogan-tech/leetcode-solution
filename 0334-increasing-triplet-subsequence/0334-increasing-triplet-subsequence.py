from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNum, secondNum = float('inf'), float('inf')
        for num in nums:
            if firstNum >= num:
                firstNum = num
            elif secondNum >= num:
                secondNum = num
            else:
                return True
        return False
        


nums = [2, 1, 5, 0, 4, 6]
print(Solution().increasingTriplet(nums))
