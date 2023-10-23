from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsCounter = list(Counter(nums).items())
        for item in numsCounter:
            if(item[1] == 1):
                return item[0]
        return 0
    
nums = [0,1,0,1,0,1,99]
print(Solution().singleNumber(nums))