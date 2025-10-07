from bisect import bisect_right, insort
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = [1 for _ in range(len(rains))]
        dryDays = []
        lakeMap = {}

        for i, rain in enumerate(rains):
            if rain == 0:
                insort(dryDays, i)
            else:
                result[i] = -1
                if rain in lakeMap:
                    j = bisect_right(dryDays, lakeMap[rain])
                    if j == len(dryDays):
                        return []
                    dryIdx = dryDays[j]
                    result[dryIdx] = rain
                    dryDays.pop(j)
                lakeMap[rain] = i

        return result


rains = [1, 2, 3, 4]
print(Solution().avoidFlood(rains))
rains = [1, 2, 0, 0, 2, 1]
print(Solution().avoidFlood(rains))
rains = [1, 2, 0, 1, 2]
print(Solution().avoidFlood(rains))
