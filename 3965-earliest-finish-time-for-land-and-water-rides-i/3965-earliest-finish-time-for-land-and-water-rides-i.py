# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        result = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                startLand = landStartTime[i]
                endLand = startLand + landDuration[i]
                startWater = max(endLand, waterStartTime[j])
                endWater = startWater + waterDuration[j]
                result = min(result, endWater)

                startWater = waterStartTime[j]
                endWater = startWater + waterDuration[j]
                startLand = max(endWater, landStartTime[i])
                endLand = startLand + landDuration[i]
                result = min(result, endLand)

        return result


'''
2 + 4 = 6
6 + 3 = 9



'''
landStartTime = [2, 8]
landDuration = [4, 1]
waterStartTime = [6]
waterDuration = [3]
print(Solution().earliestFinishTime(landStartTime,
      landDuration, waterStartTime, waterDuration))
landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]
print(Solution().earliestFinishTime(landStartTime,
      landDuration, waterStartTime, waterDuration))
