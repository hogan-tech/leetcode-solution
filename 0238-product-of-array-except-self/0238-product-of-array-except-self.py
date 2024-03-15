# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        lList, rList = [1]*length, [1]*length
        lList[0], rList[length - 1] = 1, 1
        for i in range(1, length):
            lList[i] = lList[i-1] * nums[i-1]
        for i in reversed(range(length-1)):
            rList[i] = rList[i+1] * nums[i+1]

        for i in range(length):
            lList[i] *= rList[i]

        return lList


Arrays = [-1, 1, 0, -3, 3]

print(Solution().productExceptSelf(Arrays))
