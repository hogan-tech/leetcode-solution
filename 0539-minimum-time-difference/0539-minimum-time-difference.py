from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minuteList = []
        for time in timePoints:
            minuteList.append(int(time[:2]) * 60 + int(time[3:]))
        minuteList.sort()
        result = float('inf')
        for i in range(1, len(minuteList)):
            result = min(result, minuteList[i] - minuteList[i-1])
        return min(result, 24*60 - minuteList[-1] + minuteList[0])


timePoints = ["00:00", "04:00", "22:00"]
print(Solution().findMinDifference(timePoints))
