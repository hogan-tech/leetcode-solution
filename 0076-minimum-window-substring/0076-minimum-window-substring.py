# time complexity: O(len(s) + len(t))
# space complexity: O(len(s) + len(t))
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        requireCount = defaultdict(int)
        window = defaultdict(int)
        for char in t:
            requireCount[char] += 1
        current = 0
        required = len(requireCount)
        result = [-1, -1]
        resultLen = float('inf')

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in requireCount:
                window[char] += 1
                if window[char] == requireCount[char]:
                    current += 1
            while current == required:
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = (right - left + 1)

                leftChar = s[left]
                if leftChar in requireCount:
                    window[leftChar] -= 1
                    if window[leftChar] < requireCount[leftChar]:
                        current -= 1
                left += 1
        return s[result[0]: result[1]+1] if resultLen != float('inf') else ""


S = "ADOBECODEBANC"
T = "ABC"


print(Solution().minWindow(S, T))
