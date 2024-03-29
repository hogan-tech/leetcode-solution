# time complexity: O(n)
# space complexity: O(k)
from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        counter = Counter()
        for right in range(len(s)):
            counter[s[right]] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


s = "eceba"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s, k))
