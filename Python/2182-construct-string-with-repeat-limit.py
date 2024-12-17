# time complexity: O(nlogk)
# space complexity: O(k)
from heapq import heapify, heappop, heappush
from typing import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        maxHeap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(maxHeap)
        result = []

        while maxHeap:
            charNeg, count = heappop(maxHeap)
            char = chr(-charNeg)
            use = min(count, repeatLimit)
            result.append(char * use)

            if count > use and maxHeap:
                nextCharNeg, nextCount = heappop(maxHeap)
                result.append(chr(-nextCharNeg))
                if nextCount > 1:
                    heappush(maxHeap, (nextCharNeg, nextCount - 1))
                heappush(maxHeap, (charNeg, count - use))

        return "".join(result)


s = "cczazcc"
repeatLimit = 3
print(Solution().repeatLimitedString(s, repeatLimit))
s = "aababab"
repeatLimit = 2
print(Solution().repeatLimitedString(s, repeatLimit))
