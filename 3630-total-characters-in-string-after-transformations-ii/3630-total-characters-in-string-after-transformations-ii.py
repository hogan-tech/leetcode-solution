# sigma = 26
# time complexity: O(n + logt * sigma ^ 3)
# space complexity: O(sigma ^ 2)
from typing import List


MOD = 10**9 + 7
L = 26


class Mat:
    def __init__(self, copyFrom: "Mat" = None) -> None:
        self.a: List[List[int]] = [[0] * L for _ in range(L)]
        if copyFrom:
            for i in range(L):
                for j in range(L):
                    self.a[i][j] = copyFrom.a[i][j]

    def __mul__(self, other: "Mat") -> "Mat":
        result = Mat()
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    result.a[i][j] = (
                        result.a[i][j] + self.a[i][k] * other.a[k][j]
                    ) % MOD
        return result


def I() -> Mat:
    m = Mat()
    for i in range(L):
        m.a[i][i] = 1
    return m


def quickmul(x: Mat, y: int) -> Mat:
    ans = I()
    cur = x
    while y:
        if y & 1:
            ans = ans * cur
        cur = cur * cur
        y >>= 1
    return ans


class Solution:
    def lengthAfterTransformations(
        self, s: str, t: int, nums: List[int]
    ) -> int:
        T = Mat()
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T.a[(i + j) % 26][i] = 1

        result = quickmul(T, t)

        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord("a")] += 1

        answer = 0
        for i in range(26):
            for j in range(26):
                answer = (answer + result.a[i][j] * f[j]) % MOD

        return answer


s = "abcyy"
t = 2
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
print(Solution().lengthAfterTransformations(s, t, nums))
s = "azbk"
t = 1
nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(Solution().lengthAfterTransformations(s, t, nums))
