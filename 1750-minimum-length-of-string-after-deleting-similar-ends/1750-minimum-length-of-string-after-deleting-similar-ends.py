# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right > left and s[right] == char:
                right -= 1
        return right - left + 1


s = "cabaabac"
print(Solution().minimumLength(s))
