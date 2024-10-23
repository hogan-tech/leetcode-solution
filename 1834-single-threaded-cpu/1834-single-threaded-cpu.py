# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List, Tuple


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        nextTask: List[Tuple[int, int]] = []
        result = []

        sortedTasks = [(enqueueTime, processTime, idx)
                       for idx, (enqueueTime, processTime) in enumerate(tasks)]
        sortedTasks.sort()

        currTime = 0
        taskIdx = 0
        while taskIdx < len(tasks) or nextTask:
            if not nextTask and currTime < sortedTasks[taskIdx][0]:
                currTime = sortedTasks[taskIdx][0]

            while taskIdx < len(sortedTasks) and currTime >= sortedTasks[taskIdx][0]:
                _, processTime, originalIdx = sortedTasks[taskIdx]
                heappush(nextTask, (processTime, originalIdx))
                taskIdx += 1
            processTime, index = heappop(nextTask)
            currTime += processTime
            result.append(index)

        print(sortedTasks)

        return result


tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
print(Solution().getOrder(tasks))
