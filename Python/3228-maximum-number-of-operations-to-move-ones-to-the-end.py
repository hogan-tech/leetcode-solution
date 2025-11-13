# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        result = 0
        for i, c in enumerate(s):
            if c == '1':
                count += 1
            elif i > 0 and s[i - 1] == '1':
                result += count
        return result


s = "1001101"
print(Solution().maxOperations(s))
s = "00111"
print(Solution().maxOperations(s))
