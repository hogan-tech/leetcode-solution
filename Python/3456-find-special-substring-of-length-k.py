# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s) - k + 1):
            curr = s[i:i + k]
            if len(set(curr)) == 1:
                if i > 0 and s[i - 1] == curr[0]:
                    continue
                if i + k < len(s) and s[i + k] == curr[0]:
                    continue
                return True
        return False


s = "aaafv"
k = 3
print(Solution().hasSpecialSubstring(s, k))
s = "abc"
k = 2
print(Solution().hasSpecialSubstring(s, k))
s = "h"
k = 1
print(Solution().hasSpecialSubstring(s, k))
