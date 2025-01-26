# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        inDegree = [0] * n

        for person in range(n):
            inDegree[favorite[person]] += 1

        q = deque()
        for person in range(n):
            if inDegree[person] == 0:
                q.append(person)
        depth = [1] * n

        while q:
            currentNode = q.popleft()
            nextNode = favorite[currentNode]
            depth[nextNode] = max(depth[nextNode], depth[currentNode] + 1)
            inDegree[nextNode] -= 1
            if inDegree[nextNode] == 0:
                q.append(nextNode)

        longestCycle = 0
        twoCycleInvitations = 0

        for person in range(n):
            if inDegree[person] == 0:
                continue

            cycleLength = 0
            current = person
            while inDegree[current] != 0:
                inDegree[current] = 0
                cycleLength += 1
                current = favorite[current]

            if cycleLength == 2:
                twoCycleInvitations += depth[person] + depth[favorite[person]]
            else:
                longestCycle = max(longestCycle, cycleLength)

        return max(longestCycle, twoCycleInvitations)


favorite = [2, 2, 1, 2]
print(Solution().maximumInvitations(favorite))
favorite = [1, 2, 0]
print(Solution().maximumInvitations(favorite))
favorite = [3, 0, 1, 4, 1]
print(Solution().maximumInvitations(favorite))
