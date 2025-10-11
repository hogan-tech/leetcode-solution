# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def scoreBalance(self, s: str) -> bool:
        scoreList = [0 for _ in range(len(s))]
        for i, c in enumerate(s):
            scoreList[i] = (ord(c) - ord('a') + 1)
        for i in range(len(scoreList)):
            if sum(scoreList[:i]) == sum(scoreList[i:]):
                return True
        return False


s = "adcb"
print(Solution().scoreBalance(s))
s = "bace"
print(Solution().scoreBalance(s))
s = "kl"
print(Solution().scoreBalance(s))
