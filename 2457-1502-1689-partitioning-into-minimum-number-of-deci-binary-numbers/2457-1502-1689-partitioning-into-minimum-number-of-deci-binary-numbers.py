# time complexity: O(1)
# space complexity: O(n)
from typing import Counter


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(Counter(n).keys()))


n = "32"
print(Solution().minPartitions(n))
n = "82734"
print(Solution().minPartitions(n))
n = "27346209830709182346"
print(Solution().minPartitions(n))
