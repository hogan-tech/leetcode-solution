from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [0] * len(dist)
        for i in range(len(dist)):
            time[i] = dist[i]/speed[i]
        time.sort()
        ans = 0
        for i in range(len(time)):
            if time[i] <= i:
                break
            ans += 1
        return ans


dist = [1]
speed = [1]

print(Solution().eliminateMaximum(dist, speed))
