# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        freqList = [(key, count) for key, count in freq.items()]
        freqList.sort()
        currCount = 0

        prefixFreq = defaultdict(int)
        for key, count in freqList:
            prefixFreq[key] = currCount
            currCount += count

        for i, num in enumerate(nums):
            nums[i] = prefixFreq[num]

        return nums


'''

[(1, 0), (2, 1), (3, 3), (8, 4)]
[(1, 1), (2, 2), (3, 1), (8, 1)]

'''

nums = [8, 1, 2, 2, 3]
print(Solution().smallerNumbersThanCurrent(nums))
nums = [6, 5, 4, 8]
print(Solution().smallerNumbersThanCurrent(nums))
nums = [7, 7, 7, 7]
print(Solution().smallerNumbersThanCurrent(nums))
