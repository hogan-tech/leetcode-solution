# time complexity: O(N + E)
# space complexity: O(N)
from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False for _ in range(len(rooms))]
        queue = deque()
        seen[0] = True
        queue.append(0)
        while queue:
            currRoom = queue.popleft()
            for nextRoom in rooms[currRoom]:
                if not seen[nextRoom]:
                    seen[nextRoom] = True
                    queue.append(nextRoom)
        return all(seen)


rooms = [[1], [2], [3], []]
print(Solution().canVisitAllRooms(rooms))
rooms = [[6, 7, 8], [5, 4, 9], [], [8], [4],
         [], [1, 9, 2, 3], [7], [6, 5], [2, 3, 1]]
print(Solution().canVisitAllRooms(rooms))
rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(Solution().canVisitAllRooms(rooms))
