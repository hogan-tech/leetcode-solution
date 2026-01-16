# time complexity: O(hlogh + vlogv)
# space complexity: O(logh + logv)
from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()
        hmax, vmax = 1, 1
        hcur, vcur = 1, 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                hcur += 1
            else:
                hcur = 1
            hmax = max(hmax, hcur)
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                vcur += 1
            else:
                vcur = 1
            vmax = max(vmax, vcur)
        side = min(hmax, vmax) + 1
        return side * side


n = 2
m = 1
hBars = [2, 3]
vBars = [2]
print(Solution().maximizeSquareHoleArea(n, m, hBars, vBars))
n = 1
m = 1
hBars = [2]
vBars = [2]
print(Solution().maximizeSquareHoleArea(n, m, hBars, vBars))
n = 2
m = 3
hBars = [2, 3]
vBars = [2, 4]
print(Solution().maximizeSquareHoleArea(n, m, hBars, vBars))
