# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        result = 0
        for i in range(len(processorTime)):
            result = max(result, (tasks[4*(i + 1) - 1] + processorTime[i]))
        return result


processorTime = [8, 10]
tasks = [2, 2, 3, 1, 8, 7, 4, 5]
print(Solution().minProcessingTime(processorTime, tasks))
processorTime = [10, 20]
tasks = [2, 3, 1, 2, 5, 8, 4, 3]
print(Solution().minProcessingTime(processorTime, tasks))
