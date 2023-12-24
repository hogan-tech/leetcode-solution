# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minOperations(self, s: str) -> int:
        startZero = 0
        startOne = 0
        for i in range(len(s)):
            if i % 2:
                if s[i] == '1':
                    startOne += 1
                else:
                    startZero += 1
            else:
                if s[i] == '0':
                    startOne += 1
                else:
                    startZero += 1
        return min(startOne, startZero)
s = "1111"

print(Solution().minOperations(s))
