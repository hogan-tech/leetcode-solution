# space complexity: O(n)
# time complexity: O(1)
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        maxValue = max(taskCounter.values())
        maxValueCount = list(taskCounter.values()).count(maxValue)
        return max(len(tasks), (maxValue - 1) * (n + 1) + maxValueCount)
        

'''
A: 3
B: 3

A B i A B i A B

A: 3
B: 1

A B i A i i A 

A: 3
B: 3
n = 3
A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
'''
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(Solution().leastInterval(tasks, n))
tasks = ["A", "C", "A", "B", "D", "B"]
n = 1
print(Solution().leastInterval(tasks, n))
tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
print(Solution().leastInterval(tasks, n))
