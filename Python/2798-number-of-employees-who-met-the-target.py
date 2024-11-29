from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        if len(hours) == 0:
            return 0
        sum = 0
        for i, item in enumerate(hours):
            if item >= target:
                sum += 1
        return sum


Hours = [5,1,4,2,2]
Target = 6


print(Solution().numberOfEmployeesWhoMetTarget(Hours, Target))
