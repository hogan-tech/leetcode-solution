# time complexity: O(n)
# space complexity: O(n)
from heapq import heappop, heappush


class Solution:
    def resultingString(self, s: str) -> str:
        def isConsec(a: str, b: str) -> bool:
            return (abs(ord(a) - ord(b)) == 1) or ({a, b} == {'a', 'z'})

        n = len(s)
        prev = [i - 1 for i in range(n)]
        next = [i + 1 for i in range(n)]
        prev[0] = -1
        next[-1] = -1
        valid = [True] * n

        head = 0
        pq = []
        for i in range(n - 1):
            if isConsec(s[i], s[i + 1]):
                heappush(pq, i)

        while pq:
            i = heappop(pq)
            j = next[i]
            if j == -1 or not (valid[i] and valid[j]):
                continue
            if not isConsec(s[i], s[j]):
                continue

            valid[i] = valid[j] = False
            prevI = prev[i]
            nextJ = next[j]

            if prevI != -1:
                next[prevI] = nextJ
            else:
                head = nextJ
            if nextJ != -1:
                prev[nextJ] = prevI

            if prevI != -1 and nextJ != -1 and isConsec(s[prevI], s[nextJ]):
                heappush(pq, prevI)

        result = []
        idx = head
        while idx != -1:
            if valid[idx]:
                result.append(s[idx])
            idx = next[idx]

        return "".join(result)


s = "abc"
print(Solution().resultingString(s))
s = "adcb"
print(Solution().resultingString(s))
s = "zadb"
print(Solution().resultingString(s))
