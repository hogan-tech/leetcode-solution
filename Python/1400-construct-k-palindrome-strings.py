# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        oddList = [0] * 26
        countList = [0] * 26
        for c in s:
            countList[ord(c) - ord('a')] += 1
            oddList[ord(c) - ord('a')] = countList[ord(c) - ord('a')] % 2
        if sum(oddList) > k:
            return False
        return True


s = "annabelle"
k = 2
print(Solution().canConstruct(s, k))
s = "leetcode"
k = 3
print(Solution().canConstruct(s, k))
s = "true"
k = 4
print(Solution().canConstruct(s, k))
s = "aaa"
k = 2
print(Solution().canConstruct(s, k))
