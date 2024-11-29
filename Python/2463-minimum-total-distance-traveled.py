# time complexity: O(n^2 * m)
# space complexity: O(n*m)
from typing import List


class Solution:
    def minimumTotalDistance(
        self, robot: List[int], factory: List[List[int]]
    ) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        factoryPositions = []
        for f in factory:
            factoryPositions.extend([f[0]] * f[1])
        robotCount = len(robot)
        factoryCount = len(factoryPositions)

        dp = [[None] * (factoryCount + 1) for _ in range(robotCount + 1)]

        def calculateMinDistance(robotIdx: int, factoryIdx: int) -> int:
            if dp[robotIdx][factoryIdx] is not None:
                return dp[robotIdx][factoryIdx]
            if robotIdx == robotCount:
                dp[robotIdx][factoryIdx] = 0
                return 0
            if factoryIdx == factoryCount:
                dp[robotIdx][factoryIdx] = int(1e12)
                return int(1e12)

            assign = abs(
                robot[robotIdx] - factoryPositions[factoryIdx]
            ) + calculateMinDistance(robotIdx + 1, factoryIdx + 1)

            skip = calculateMinDistance(robotIdx, factoryIdx + 1)

            dp[robotIdx][factoryIdx] = min(assign, skip)
            return dp[robotIdx][factoryIdx]

        return calculateMinDistance(0, 0)


robot = [0, 4, 6]
factory = [[2, 2], [6, 2]]
print(Solution().minimumTotalDistance(robot, factory))
