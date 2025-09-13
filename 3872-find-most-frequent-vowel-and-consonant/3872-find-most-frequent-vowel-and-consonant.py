# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelFreq = defaultdict(int)
        consonantFreq = defaultdict(int)
        vowelFreq['a'] = 0
        consonantFreq['b'] = 0
        for c in s:
            if c in 'aeiou':
                vowelFreq[c] += 1
            else:
                consonantFreq[c] += 1
        return max(vowelFreq.values()) + max(consonantFreq.values())


s = "successes"
print(Solution().maxFreqSum(s))
s = "aeiaeia"
print(Solution().maxFreqSum(s))
