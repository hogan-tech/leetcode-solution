# time complexity: O(nlogc) = O(n)
# space complexity: O(1)
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        result = []
        maxHeap = [(-value, char) for char, value in Counter(s).items()]
        heapify(maxHeap)
        previous = None
        while maxHeap or previous:
            if previous and len(maxHeap) == 0:
                return ""
            currValue, currChar = heappop(maxHeap)
            result.append(currChar)
            currValue += 1

            if previous:
                heappush(maxHeap, previous)
                previous = None

            if currValue != 0:
                previous = (currValue, currChar)

        return "".join(result)


s = "bbnnc"
print(Solution().reorganizeString(s))
s = "aaab"
print(Solution().reorganizeString(s))
