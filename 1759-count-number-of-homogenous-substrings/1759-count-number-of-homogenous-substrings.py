# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        currStreak = 0
        MOD = 10 ** 9 + 7
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                currStreak += 1
            else:
                currStreak = 1
            ans = (ans + currStreak) % MOD
        return ans


s = "abbcccaa"
print(Solution().countHomogenous(s))
