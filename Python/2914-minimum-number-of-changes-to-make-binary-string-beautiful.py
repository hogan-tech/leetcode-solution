# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minChanges(self, s: str) -> int:
        currentChar = s[0]
        consecutiveCount = 0
        minChangesRequired = 0

        for char in s:
            if char == currentChar:
                consecutiveCount += 1
                continue
            if consecutiveCount % 2 == 0:
                consecutiveCount = 1
            else:
                consecutiveCount = 0
                minChangesRequired += 1
            currentChar = char
        return minChangesRequired


s = "1001"
print(Solution().minChanges(s))
