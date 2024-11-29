# time complexity: O(m*(n+m))
# space complexity: O(n + M)
from cmath import inf
from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))

        while q:
            person, time = q.popleft()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    q.append((next_person, t))

        return [i for i in range(n) if earliest[i] != inf]


n = 6
meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
firstPerson = 1
print(Solution().findAllPeople(n, meetings, firstPerson))
