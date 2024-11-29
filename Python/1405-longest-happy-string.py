# time complexity: O(a+b+c)
# space complexity: O(1)
from heapq import heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heappush(pq, (-a, 'a'))
        if b > 0:
            heappush(pq, (-b, 'b'))
        if c > 0:
            heappush(pq, (-c, 'c'))
        result = []
        while pq:
            freq, char = heappop(pq)
            freq = -freq
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                if not pq:
                    break
                tempFreq, tempChar = heappop(pq)
                result.append(tempChar)
                if tempFreq + 1 < 0:
                    heappush(pq, (tempFreq + 1, tempChar))
                heappush(pq, (-freq, char))
            else:
                freq -= 1
                result.append(char)
                if freq > 0:
                    heappush(pq, (-freq, char))
        return "".join(result)


a = 1
b = 1
c = 7
print(Solution().longestDiverseString(a, b, c))
