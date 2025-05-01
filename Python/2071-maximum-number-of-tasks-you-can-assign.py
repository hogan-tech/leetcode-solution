# time complexity: O(nlogn + mlogm + min(m,n)log^2min(m,n))
# space complexity: O(logn + logm + min(m, n))
from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            p = pills
            ws = SortedList(workers[m - mid:])
            for i in range(mid - 1, -1, -1):
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


tasks = [3, 2, 1]
workers = [0, 3, 3]
pills = 1
strength = 1
print(Solution().maxTaskAssign(tasks, workers, pills, strength))
tasks = [5, 4]
workers = [0, 0, 0]
pills = 1
strength = 5
print(Solution().maxTaskAssign(tasks, workers, pills, strength))
tasks = [10, 15, 30]
workers = [0, 10, 10, 10, 10]
pills = 3
strength = 10
print(Solution().maxTaskAssign(tasks, workers, pills, strength))
