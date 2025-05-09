# time complexity: O(n^2*s)
# space complexity: O(n^2 + n*s)
from math import comb


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        total, n = 0, len(num)
        cnt = [0] * 10
        for c in num:
            digit = int(c)
            cnt[digit] += 1
            total += digit
        if total % 2 != 0:
            return 0

        target = total // 2
        maxOdd = (n + 1) // 2
        f = [[0] * (maxOdd + 1) for _ in range(target + 1)]
        f[0][0] = 1
        psum = totSum = 0
        for i in range(10):
            psum += cnt[i]

            totSum += i * cnt[i]
            for oddCnt in range(min(psum, maxOdd), max(0, psum - (n - maxOdd)) - 1, -1):
                evenCnt = psum - oddCnt
                for curr in range(min(totSum, target), max(0, totSum - target) - 1, -1):
                    result = 0
                    for j in range(max(0, cnt[i] - evenCnt), min(cnt[i], oddCnt) + 1):
                        if i * j > curr:
                            break
                        ways = (comb(oddCnt, j) *
                                comb(evenCnt, cnt[i] - j) % MOD)
                        result = (result + ways *
                                  f[curr - i * j][oddCnt - j] % MOD) % MOD
                    f[curr][oddCnt] = result % MOD

        return f[target][maxOdd]


num = "962698867371637231389"
print(Solution().countBalancedPermutations(num))
