# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush


class Solution:
    def largestInteger(self, num: int) -> int:
        oddHeap = []
        evenHeap = []
        result = 0
        for c in str(num):
            if int(c) % 2:
                heappush(oddHeap, -int(c))
            else:
                heappush(evenHeap, -int(c))

        for c in str(num):
            result *= 10
            if int(c) % 2:
                result += -heappop(oddHeap)
            else:
                result += -heappop(evenHeap)
            

        return result


num = 1234
print(Solution().largestInteger(num))
num = 65875
print(Solution().largestInteger(num))
