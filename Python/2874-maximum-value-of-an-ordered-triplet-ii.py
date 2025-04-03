# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefixMaxList = []
        suffixMaxList = []
        currPrefixMax = float('-inf')
        currSuffixMax = float('-inf')

        for num in nums:
            currPrefixMax = max(currPrefixMax, num)
            prefixMaxList.append(currPrefixMax)
        for num in nums[::-1]:
            currSuffixMax = max(currSuffixMax, num)
            suffixMaxList.append(currSuffixMax)
        suffixMaxList = suffixMaxList[::-1]

        result = float('-inf')
        for i in range(1, len(nums) - 1):
            result = max(
                result, (prefixMaxList[i - 1] - nums[i]) * suffixMaxList[i + 1])
        return 0 if result < 0 else result


# (12 - 1) * 7
nums = [12, 6, 1, 2, 7]
print(Solution().maximumTripletValue(nums))
# (10 - 3) * 19
nums = [1, 10, 3, 4, 19]
print(Solution().maximumTripletValue(nums))
# (1 - 2) * 3
nums = [1, 2, 3]
print(Solution().maximumTripletValue(nums))
# (13 - 6) * 2
nums = [10, 13, 6, 2]
print(Solution().maximumTripletValue(nums))
