# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List
import bisect


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        waterRides = list(zip(waterStartTime, waterDuration))
        waterRides.sort()
        waterStarts = [x[0] for x in waterRides]
        waterDurations = [x[1] for x in waterRides]
        waterTotals = [x[0] + x[1] for x in waterRides]

        prefixMinDuration = []
        minDur = float('inf')
        for dur in waterDurations:
            if dur < minDur:
                minDur = dur
            prefixMinDuration.append(minDur)

        suffixMinTotal = [float('inf')] * (len(waterRides) + 1)
        for i in range(len(waterRides) - 1, -1, -1):
            suffixMinTotal[i] = min(waterTotals[i], suffixMinTotal[i + 1])

        result1 = float('inf')
        for landStart, landDur in zip(landStartTime, landDuration):
            landFinish = landStart + landDur
            idx = bisect.bisect_right(waterStarts, landFinish) - 1
            currentMin = float('inf')
            if idx >= 0:
                currentMin = landFinish + prefixMinDuration[idx]
            if idx + 1 < len(waterRides):
                candidate = suffixMinTotal[idx + 1]
                if candidate < currentMin:
                    currentMin = candidate
            if currentMin < result1:
                result1 = currentMin

        landRides = list(zip(landStartTime, landDuration))
        landRides.sort()
        landStarts = [x[0] for x in landRides]
        landDurations = [x[1] for x in landRides]
        landTotals = [x[0] + x[1] for x in landRides]

        prefixMinDurationLand = []
        minDur = float('inf')
        for dur in landDurations:
            if dur < minDur:
                minDur = dur
            prefixMinDurationLand.append(minDur)

        suffixMinTotalLand = [float('inf')] * (len(landRides) + 1)
        for i in range(len(landRides) - 1, -1, -1):
            suffixMinTotalLand[i] = min(
                landTotals[i], suffixMinTotalLand[i + 1])

        result2 = float('inf')
        for waterStart, waterDur in zip(waterStartTime, waterDuration):
            waterFinish = waterStart + waterDur
            idx = bisect.bisect_right(landStarts, waterFinish) - 1
            currentMin = float('inf')
            if idx >= 0:
                currentMin = waterFinish + prefixMinDurationLand[idx]
            if idx + 1 < len(landRides):
                candidate = suffixMinTotalLand[idx + 1]
                if candidate < currentMin:
                    currentMin = candidate
            if currentMin < result2:
                result2 = currentMin

        return min(result1, result2)


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
landStartTime = [8, 48]
landDuration = [28, 63]
waterStartTime = [61, 87, 24, 75, 64]
waterDuration = [31, 58, 71, 67, 13]
print(Solution().earliestFinishTime(landStartTime,
      landDuration, waterStartTime, waterDuration))
