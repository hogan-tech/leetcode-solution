# time complexity: O(1)
# space complexity: O(1)
from typing import Optional


class Solution:
    def specialPalindrome(self, n: int) -> int:
        s = str(n)
        lenN = len(s)

        validByLen = {}
        for mask in range(1, 1 << 9):
            counts = [0] * 10
            oddCnt = 0
            totalLen = 0
            for i in range(9):
                d = i + 1
                if mask & (1 << i):
                    counts[d] = d
                    totalLen += d
                    if d % 2 == 1:
                        oddCnt += 1
            if oddCnt <= 1:
                validByLen.setdefault(totalLen, []).append(tuple(counts))

        def buildMinPalFromCounts(countsTuple) -> str:
            counts = list(countsTuple)
            firstHalf = []
            mid = ''
            for d in range(1, 10):
                if counts[d] % 2 == 1:
                    mid = str(d)
                firstHalf.append(str(d) * (counts[d] // 2))
            firstHalfStr = "".join(firstHalf)
            return firstHalfStr + mid + firstHalfStr[::-1]

        def nextPalFromCounts(countsTuple, target: str) -> Optional[str]:
            L = len(target)
            counts = list(countsTuple)
            half = L // 2
            first = [''] * half

            def canUsePair(d: int) -> bool:
                return counts[d] >= 2

            def usePair(d: int, delta: int):
                counts[d] += delta

            def middleOptions():
                if L % 2 == 0:
                    return ['']
                opts = []
                for d in range(1, 10):
                    if counts[d] == 1:
                        opts.append(str(d))
                return sorted(opts)

            temp = target

            def dfs(i: int, greater: bool) -> Optional[str]:
                if i == half:
                    for midDigit in middleOptions():
                        if not greater:
                            if L % 2 == 1:
                                cMid = int(midDigit) if midDigit else -1
                                sMid = int(temp[i])
                                if cMid < sMid:
                                    continue
                                g2 = greater or (cMid > sMid)
                            else:
                                g2 = greater
                        else:
                            g2 = True

                        left = "".join(first)
                        pal = left + midDigit + \
                            left[::-1] if L % 2 == 1 else left + left[::-1]
                        if pal > temp:
                            return pal
                    return None

                low = int(temp[i]) if not greater else 1
                for d in range(max(1, low), 10):
                    if canUsePair(d):
                        usePair(d, -2)
                        first[i] = str(d)
                        g2 = greater or (d > int(temp[i]))
                        res = dfs(i + 1, g2)
                        if res is not None:
                            return res
                        usePair(d, +2)
                        first[i] = ''
                return None

            return dfs(0, False)

        best = None

        currl = lenN
        if currl in validByLen:
            for counts in validByLen[currl]:
                cand = nextPalFromCounts(counts, s)
                if cand is not None:
                    if best is None or (len(cand) < len(best)) or (len(cand) == len(best) and cand < best):
                        best = cand

        if best is None:
            for currl in range(lenN + 1, 46):
                if currl not in validByLen:
                    continue
                for counts in validByLen[currl]:
                    pal = buildMinPalFromCounts(counts)
                    if best is None or pal < best:
                        best = pal
                if best is not None:
                    break

        return int(best)


n = 2
print(Solution().specialPalindrome(n))
n = 33
print(Solution().specialPalindrome(n))
