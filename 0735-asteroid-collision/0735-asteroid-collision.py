# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while len(stack) > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if len(stack) == 0:
                    result.append(asteroid)
                else:
                    if stack[-1] == abs(asteroid):
                        stack.pop()
        result += stack
        return result



asteroids = [10, 2, -5]
print(Solution().asteroidCollision(asteroids))
