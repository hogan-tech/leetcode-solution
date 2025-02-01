# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        gaps = []
        gaps.append(startTime[0])
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        if n == 0:
            return eventTime

        result = 0
        windowSum = sum(gaps[:k+1])
        result = max(result, windowSum)
        for i in range(k + 1, len(gaps)):
            windowSum += gaps[i] - gaps[i - (k + 1)]
            result = max(result, windowSum)

        return result


eventTime = 5
k = 1
startTime = [1, 3]
endTime = [2, 5]
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))  # 2
eventTime = 10
k = 1
startTime = [0, 2, 9]
endTime = [1, 4, 10]
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))  # 6
eventTime = 5
k = 2
startTime = [0, 1, 2, 3, 4]
endTime = [1, 2, 3, 4, 5]
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))  # 0
eventTime = 99
k = 1
startTime = [7, 21, 25]
endTime = [13, 25, 78]
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))  # 21
eventTime = 64
k = 2
startTime = [29, 49]
endTime = [37, 54]
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))  # 51
eventTime = 83
k = 1
startTime = [13, 15, 43, 81]
endTime = [15, 22, 78, 83]
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))  # 24
