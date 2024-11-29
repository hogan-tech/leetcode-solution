# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        beg = 0
        end = start[-1] - start[0] + d
        while beg <= end:
            mid = (beg + end) // 2
            pos = True
            prev = float('-inf')
            for s in start:
                curr = min(max(prev + mid, s), s + d)
                if s <= curr <= s + d and curr >= prev + mid:
                    prev = curr
                else:
                    pos = False
                    break
            if pos:
                beg = mid + 1
            else:
                end = mid - 1
        return beg - 1


start = [6, 0, 3]
d = 2
print(Solution().maxPossibleScore(start, d))
