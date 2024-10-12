from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num == 2:
                ans.append(-1)
                continue

            numCopy = num
            count = 0

            while num & 1 == 1:
                count += 1
                num >>= 1

            ans.append(numCopy - 2 ** (count-1))

        return ans
