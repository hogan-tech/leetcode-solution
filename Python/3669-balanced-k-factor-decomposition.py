# time complexity: O(n^1/n + n^k/n * k)
# space complexity: O(n^1/n + k)
from typing import List


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        def getDivisors(x):
            divs = set()
            for i in range(1, int(x ** 0.5) + 1):
                if x % i == 0:
                    divs.add(i)
                    divs.add(x // i)
            return list(divs)

        divisors = getDivisors(n)
        best = []
        minDiff = float('inf')

        def dfs(start, path, currProd):
            nonlocal best, minDiff
            if len(path) == k:
                if currProd == n:
                    diff = max(path) - min(path)
                    if diff < minDiff:
                        minDiff = diff
                        best = path[:]
                return
            for i in range(start, len(divisors)):
                d = divisors[i]
                if currProd * d > n:
                    continue
                if n % (currProd * d) != 0:
                    continue
                dfs(i, path + [d], currProd * d)

        divisors.sort()
        dfs(0, [], 1)
        return best


n = 100
k = 2
print(Solution().minDifference(n, k))
n = 44
k = 3
print(Solution().minDifference(n, k))
