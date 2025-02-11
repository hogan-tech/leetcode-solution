# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userLog = defaultdict(set)
        result = [0 for _ in range(k)]
        for user, log in logs:
            userLog[user].add(log)
        for user, logSet in userLog.items():
            UAM = len(logSet)
            result[UAM - 1] += 1
        return result


logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k = 5
print(Solution().findingUsersActiveMinutes(logs, k))
logs = [[1, 1], [2, 2], [2, 3]]
k = 4
print(Solution().findingUsersActiveMinutes(logs, k))
