# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        N = len(arr)
        visited = set()
        queue.append(start)
        visited.add(start)
        while queue:
            curr = queue.pop()
            prev = curr - arr[curr]
            next = curr + arr[curr]
            if arr[curr] == 0:
                return True
            if 0 <= prev < N and prev not in visited:
                queue.append(prev)
                visited.add(prev)
            if 0 <= next < N and next not in visited:
                queue.append(next)
                visited.add(next)
        return False


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(Solution().canReach(arr, start))
arr = [4, 2, 3, 0, 3, 1, 2]
start = 0
print(Solution().canReach(arr, start))
arr = [3, 0, 2, 1, 2]
start = 2
print(Solution().canReach(arr, start))
arr = [0]
start = 0
print(Solution().canReach(arr, start))
