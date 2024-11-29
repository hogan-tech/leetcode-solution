# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def findAnagrams(self, original: str, target: str) -> List[int]:
        result = []
        originalLen = len(original)
        targetLen = len(target)
        freqOriginal = Counter(original[:targetLen])
        freqTarget = Counter(target)
        left = 1
        right = targetLen
        if freqOriginal == freqTarget:
            result.append(0)
        while right < originalLen:
            freqOriginal[original[left - 1]] -= 1
            freqOriginal[original[right]] += 1
            if freqOriginal == freqTarget:
                result.append(left)
            right += 1
            left += 1

        return result


s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
