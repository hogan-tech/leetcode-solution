# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        if len(s) < k:
            return 0

        count = 0
        for i in range(k):
            freq[s[i]] += 1

        if len(freq) == k:
            count += 1

        for i in range(1, len(s) - k + 1):

            prevWord = s[i - 1]
            newWord = s[i + k - 1]

            freq[prevWord] -= 1
            freq[newWord] += 1
            if freq[prevWord] == 0:
                del freq[prevWord]

            if len(freq) == k:
                count += 1

        return count


s = "havefunonleetcode"
k = 5
print(Solution().numKLenSubstrNoRepeats(s, k))
s = "home"
k = 5
print(Solution().numKLenSubstrNoRepeats(s, k))
s = "abab"
k = 2
print(Solution().numKLenSubstrNoRepeats(s, k))
