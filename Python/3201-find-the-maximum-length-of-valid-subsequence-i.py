# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        oddEvenList = [num % 2 for num in nums]
        oddCount = oddEvenList.count(1)
        evenCount = oddEvenList.count(0)
        oddFirstCount = 0
        oddFirstFlag = 1
        evenFirstCount = 0
        evenFirstFlag = 0
        for num in oddEvenList:
            if num == oddFirstFlag:
                oddFirstCount += 1
                oddFirstFlag = (oddFirstCount + 1) % 2
            if num == evenFirstFlag:
                evenFirstCount += 1
                evenFirstFlag = (evenFirstFlag + 1) % 2

        return max(oddCount, evenCount, oddFirstCount, evenFirstCount)


'''
1 0 1 0

1 0 1 1 0 1 0

1 1
'''
nums = [1, 2, 3, 4]
print(Solution().maximumLength(nums))
nums = [1, 2, 1, 1, 2, 1, 2]
print(Solution().maximumLength(nums))
nums = [1, 3]
print(Solution().maximumLength(nums))
