# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        logsStack = []
        result = [0] * n
        for log in logs:
            id, operation, time = log.split(':')
            logId = int(id)
            logTime = int(time)
            if operation == 'start':
                logsStack.append((logId, logTime))
            else:
                topId, topTime = logsStack.pop()
                result[topId] += (logTime - topTime) + 1
                if logsStack:
                    result[logsStack[-1][0]] -= (logTime - topTime + 1)
        return result


n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
print(Solution().exclusiveTime(n, logs))
n = 1
logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
print(Solution().exclusiveTime(n, logs))
