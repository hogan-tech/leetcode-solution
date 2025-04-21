# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        visited = set()
        i = 0

        while 0 <= i < len(instructions) and i not in visited:
            visited.add(i)
            if instructions[i] == "add":
                score += values[i]
                i += 1
            elif instructions[i] == "jump":
                i += values[i]
            else:
                break

        return score


instructions = ["jump", "add", "add", "jump", "add", "jump"]
values = [2, 1, 3, 1, -2, -3]
print(Solution().calculateScore(instructions, values))
instructions = ["jump", "add", "add"]
values = [3, 1, 1]
print(Solution().calculateScore(instructions, values))
instructions = ["jump"]
values = [0]
print(Solution().calculateScore(instructions, values))
