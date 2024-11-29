# space complexity: O(n)
# time complexity: O(1)
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxFreq = max(taskCount.values())
        nMax = list(taskCount.values()).count(maxFreq)
        return max(len(tasks), (maxFreq-1)*(n+1) + nMax)


Tasks = ["A", "A", "A", "B", "B", "B"]
N = 2


print(Solution().leastInterval(Tasks, N))
