# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ans = [0] * n
        times = [0] * n
        meetings.sort()
        for start, end in meetings:
            flag = False
            minind = -1
            val = float('inf')
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break
            if not flag:
                ans[minind] += 1
                times[minind] += (end - start)
        maxi = -1
        id = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i
        return id


n = 3
meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
print(Solution().mostBooked(n, meetings))
