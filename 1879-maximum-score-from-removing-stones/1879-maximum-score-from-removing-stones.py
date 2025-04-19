# time complexity: O(n)
# space complexity: O(1)
from heapq import heapify, heappop, heappush


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        result = 0
        heap = [-a, -b, -c]
        heapify(heap)

        while len(heap) > 1:
            num1 = -heappop(heap) - 1
            num2 = -heappop(heap) - 1
            if num1 > 0:
                heappush(heap, -num1)
            if num2 > 0:
                heappush(heap, -num2)
            result += 1

        return result


a = 2
b = 4
c = 6
print(Solution().maximumScore(a, b, c))
a = 4
b = 4
c = 6
print(Solution().maximumScore(a, b, c))
a = 1
b = 8
c = 7
print(Solution().maximumScore(a, b, c))
