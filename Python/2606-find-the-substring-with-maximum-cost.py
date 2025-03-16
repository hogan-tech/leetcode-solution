# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        charMap = defaultdict(int)
        for i in range(len(chars)):
            charMap[chars[i]] = vals[i]
        for i in range(26):
            alpha = chr(i + ord('a'))
            val = i + 1
            if alpha not in charMap:
                charMap[alpha] = val

        currSum = 0
        result = 0
        for c in s:
            currSum += charMap[c]
            if currSum < 0:
                currSum = 0
            result = max(result, currSum)
        return result


s = "adaa"
chars = "d"
vals = [-1000]
print(Solution().maximumCostSubstring(s, chars, vals))
s = "abc"
chars = "abc"
vals = [-1, -1, -1]
print(Solution().maximumCostSubstring(s, chars, vals))
