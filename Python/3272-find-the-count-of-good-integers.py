# time complexity: O(nlogn * 10^m)
# space complexity: O(n * 10^m)
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        numSet = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            if palindromicInteger % k == 0:
                sortedList = "".join(sorted(s))
                numSet.add(sortedList)

        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in numSet:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            total = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                total //= fac[x]
            ans += total

        return ans


n = 3
k = 5
print(Solution().countGoodIntegers(n, k))
n = 1
k = 4
print(Solution().countGoodIntegers(n, k))
n = 5
k = 6
print(Solution().countGoodIntegers(n, k))
