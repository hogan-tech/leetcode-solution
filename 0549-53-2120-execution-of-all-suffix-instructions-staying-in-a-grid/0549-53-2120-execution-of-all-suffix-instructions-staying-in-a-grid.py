# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        sLen = len(s)
        dirDict = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
        for _ in range(sLen):
            count = 0
            currR, currC = startPos
            for c in s:
                currR += dirDict[c][0]
                currC += dirDict[c][1]
                if 0 <= currR < n and 0 <= currC < n:
                    count += 1
                else:
                    break
            s = s[1:]
            result.append(count)
        return result


n = 3
startPos = [0, 1]
s = "RRDDLU"
print(Solution().executeInstructions(n, startPos, s))
n = 2
startPos = [1, 1]
s = "LURD"
print(Solution().executeInstructions(n, startPos, s))
n = 1
startPos = [0, 0]
s = "LRUD"
print(Solution().executeInstructions(n, startPos, s))
