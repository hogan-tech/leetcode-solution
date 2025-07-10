# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(
                t2,
                (eventTime if i == 0 else startTime[n - i])
                - endTime[n - i - 1],
            )

        result = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                result = max(result, right - left)
            else:
                result = max(result, right - left -
                             (endTime[i] - startTime[i]))
        return result


eventTime = 5
startTime = [1, 3]
endTime = [2, 5]
print(Solution().maxFreeTime(eventTime, startTime, endTime))
eventTime = 10
startTime = [0, 7, 9]
endTime = [1, 8, 10]
print(Solution().maxFreeTime(eventTime, startTime, endTime))
eventTime = 10
startTime = [0, 3, 7, 9]
endTime = [1, 4, 8, 10]
print(Solution().maxFreeTime(eventTime, startTime, endTime))
eventTime = 5
startTime = [0, 1, 2, 3, 4]
endTime = [1, 2, 3, 4, 5]
print(Solution().maxFreeTime(eventTime, startTime, endTime))
