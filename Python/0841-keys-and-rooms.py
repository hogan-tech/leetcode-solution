# time complexity: O(N + E)
# space complexity: O(N)
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        canVisit = [False] * len(rooms)
        canVisit[0] = True
        stack = [0]
        while stack:
            for nextIdx in rooms[stack.pop()]:
                if canVisit[nextIdx] is False:
                    canVisit[nextIdx] = True
                    stack.append(nextIdx)
        return all(canVisit)


rooms = [[6, 7, 8], [5, 4, 9], [], [8], [4],
         [], [1, 9, 2, 3], [7], [6, 5], [2, 3, 1]]
print(Solution().canVisitAllRooms(rooms))
