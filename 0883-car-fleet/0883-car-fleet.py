# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(Solution().carFleet(target, position, speed))
target = 10
position = [3]
speed = [3]
print(Solution().carFleet(target, position, speed))
target = 100
position = [0, 2, 4]
speed = [4, 2, 1]
print(Solution().carFleet(target, position, speed))
