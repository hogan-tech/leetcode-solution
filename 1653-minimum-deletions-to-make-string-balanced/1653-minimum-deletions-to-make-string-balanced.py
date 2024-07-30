# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        aCount = s.count('a')
        bCount, minDel = 0, len(s)
        for ch in s:
            if ch == 'a':
                aCount -= 1
            minDel = min(minDel, aCount + bCount)
            if ch == 'b':
                bCount += 1
        return minDel


s = "aababbab"
print(Solution().minimumDeletions(s))
