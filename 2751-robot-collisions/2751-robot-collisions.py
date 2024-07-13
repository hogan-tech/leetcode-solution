# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        robotsIdx = list(range(len(positions)))
        robotsIdx.sort(key=lambda x: positions[x])
        for currIdx in robotsIdx:
            if directions[currIdx] == "R":
                stack.append(currIdx)
            else:
                while stack and healths[currIdx] > 0:
                    topIdx = stack.pop()
                    if healths[topIdx] > healths[currIdx]:
                        healths[topIdx] -= 1
                        healths[currIdx] = 0
                        stack.append(topIdx)
                    elif healths[topIdx] < healths[currIdx]:
                        healths[currIdx] -= 1
                        healths[topIdx] = 0
                    else:
                        healths[currIdx] = 0
                        healths[topIdx] = 0

        return [health for health in healths if health > 0]


positions = [3, 5, 2, 6]
healths = [10, 10, 15, 12]
directions = "RLRL"
print(Solution().survivedRobotsHealths(positions, healths, directions))
