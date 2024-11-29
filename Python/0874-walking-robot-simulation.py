# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}
        x, y = 0, 0
        curDir, distance = 0, 0
        obstaclesSet = set(tuple(o) for o in obstacles)
        for command in commands:
            if command == -1:
                curDir += 90
            elif command == -2:
                curDir -= 90
            else:
                curDir %= 360
                dx, dy = directions[curDir]
                for _ in range(command):
                    if (x + dx, y + dy) in obstaclesSet:
                        break
                    x += dx
                    y += dy
                distance = max(distance, x**2 + y**2)
        return distance


commands = [6, -1, -1, 6]
obstacles = []

print(Solution().robotSim(commands, obstacles))
