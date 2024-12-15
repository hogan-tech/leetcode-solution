# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        maxTime = 0
        buttonIdx = -1
        for i in range(len(events)):
            if i == 0:
                currTime = events[i][1]
            else:
                currTime = events[i][1] - events[i-1][1]

            if currTime > maxTime or (currTime == maxTime and events[i][0] < buttonIdx):
                maxTime = currTime
                buttonIdx = events[i][0]
        return buttonIdx


events = [[1, 2], [2, 5], [3, 9], [1, 15]]
print(Solution().buttonWithLongestTime(events))
events = [[10, 5], [1, 7]]
print(Solution().buttonWithLongestTime(events))
