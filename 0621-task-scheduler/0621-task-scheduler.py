from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxFeq = max(taskCount.values())
        nMax = list(taskCount.values()).count(maxFeq)
        return max(len(tasks), (maxFeq-1) * (n+1) + nMax)