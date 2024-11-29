# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        lenN = len(n)
        i = lenN // 2 - 1 if lenN % 2 == 0 else lenN // 2
        firstHalf = int(n[: i + 1])
        possibilities = []
        possibilities.append(
            self.halfToPalindrome(firstHalf, lenN % 2 == 0)
        )
        possibilities.append(
            self.halfToPalindrome(firstHalf + 1, lenN % 2 == 0)
        )
        possibilities.append(
            self.halfToPalindrome(firstHalf - 1, lenN % 2 == 0)
        )
        possibilities.append(10 ** (lenN - 1) - 1)
        possibilities.append(10**lenN + 1)

        diff = float("inf")
        res = 0
        nl = int(n)
        for cand in possibilities:
            if cand == nl:
                continue
            if abs(cand - nl) < diff:
                diff = abs(cand - nl)
                res = cand
            elif abs(cand - nl) == diff:
                res = min(res, cand)
        return str(res)

    def halfToPalindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left = left // 10
        while left > 0:
            res = res * 10 + left % 10
            left //= 10
        return res


n = "123"
print(Solution().nearestPalindromic(n))
