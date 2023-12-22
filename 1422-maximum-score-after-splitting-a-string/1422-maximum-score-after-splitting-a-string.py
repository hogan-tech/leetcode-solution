# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0
        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans


s = "011101"
print(Solution().maxScore(s))
