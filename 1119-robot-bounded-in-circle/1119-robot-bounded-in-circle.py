# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = instructions * 4
        DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        currPosition = [0, 0]
        currDir = 0
        for instruction in instructions:
            if instruction == 'G':
                currPosition = [currPosition[0] + DIRS[currDir]
                                [0], currPosition[1] + DIRS[currDir][1]]
            if instruction == 'L':
                currDir = (currDir + 1 + 4) % 4
            if instruction == 'R':
                currDir = (currDir - 1 + 4) % 4

        return currPosition == [0, 0]


instructions = "GGLLGG"
print(Solution().isRobotBounded(instructions))
instructions = "GG"
print(Solution().isRobotBounded(instructions))
instructions = "GL"
print(Solution().isRobotBounded(instructions))
