from functools import lru_cache


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        d = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25
        }

        MOD = 10**9 + 7
        ans = 0
        memo = {}

        def count(c):
            if c < 26:
                return 1
            if c in memo:
                return memo[c]
            temp = count(c-26) + count(c-25)
            memo[c] = temp
            return temp

        for l in s:
            ans += count(d[l]+t)
        return ans % MOD


s = "abcyy"
t = 26
print(Solution().lengthAfterTransformations(s, t))
s = "azbk"
t = 1
print(Solution().lengthAfterTransformations(s, t))
s = "jqktcurgdvlibczdsvnsg"
t = 5
print(Solution().lengthAfterTransformations(s, t))
s = "jqktcurgdvlibczdsvnsg"
t = 480
print(Solution().lengthAfterTransformations(s, t))
