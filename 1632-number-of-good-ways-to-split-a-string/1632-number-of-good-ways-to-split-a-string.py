# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        rightFreq = defaultdict(int)
        for c in s:
            rightFreq[c] += 1
        leftFreq = defaultdict(int)
        result = 0
        for c in s:
            rightFreq[c] -= 1
            if rightFreq[c] == 0:
                del rightFreq[c]
            leftFreq[c] += 1
            if len(rightFreq) == len(leftFreq):
                result += 1
        return result


s = "aacaba"
print(Solution().numSplits(s))
s = "abcd"
print(Solution().numSplits(s))
