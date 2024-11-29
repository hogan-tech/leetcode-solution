# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left, right = 0,0
        freq = {}
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0
            freq[s[right]] += 1

            windowSize = right - left + 1

            if windowSize - max(freq.values()) <= k:
                result = max(result, windowSize)
            else:
                freq[s[left]] -= 1
                if not freq[s[left]]:
                    freq.pop(s[left])
                left += 1

        return result

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))