# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        backToMain = 0
        for log in logs:
            if log == "../":
                if backToMain > 0:
                    backToMain -= 1
            elif log == "./":
                backToMain += 0
            else:
                backToMain += 1
        return 0 if backToMain < 0 else backToMain


logs = ["./", "wz4/", "../", "mj2/", "../", "../", "ik0/", "il7/"]
print(Solution().minOperations(logs))
