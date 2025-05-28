# time complexity: O(n^2)
# space complexity: O(n^2)
from collections import defaultdict, deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)

        queue = deque()
        queue.append([headID, informTime[headID]])
        result = 0
        while queue:
            currNode, currTime = queue.popleft()
            for nextNode in adj[currNode]:
                queue.append([nextNode, currTime + informTime[nextNode]])
                result = max(result, currTime + informTime[nextNode])

        return result


n = 1
headID = 0
manager = [-1]
informTime = [0]
print(Solution().numOfMinutes(n, headID, manager, informTime))
n = 6
headID = 2
manager = [2, 2, -1, 2, 2, 2]
informTime = [0, 0, 1, 0, 0, 0]
print(Solution().numOfMinutes(n, headID, manager, informTime))
