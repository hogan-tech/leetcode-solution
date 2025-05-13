# time complexity: O(nlog(logn))
# space complexity: O(n)
from math import sqrt


TOTAL = 10 ** 6
prime = [False, False] + [True] * (TOTAL - 1)
for i in range(2, int(sqrt(TOTAL)) + 1):
    if prime[i]:
        for j in range(i * 2, TOTAL, i):
            prime[j] = False


class Solution(object):
    def findPrimePairs(self, n):
        if n < 4:
            return []
        result = []
        for i in range(2, (n // 2) + 1):
            remain = n - i
            if prime[i] and prime[remain]:
                result.append([i, remain])

        return result


n = 10
print(Solution().findPrimePairs(n))
n = 2
print(Solution().findPrimePairs(n))
n = 247
print(Solution().findPrimePairs(n))
