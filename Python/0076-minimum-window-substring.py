# time complexity: O(len(s) + len(t))
# space complexity: O(len(s) + len(t))
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        feqCount = defaultdict(int)
        window = defaultdict(int)
        result = [-1, -1]
        resultLen = float('inf')
        current = 0

        for char in t:
            feqCount[char] += 1

        required = len(feqCount)

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in feqCount:
                window[char] += 1
                if window[char] == feqCount[char]:
                    current += 1
            while current == required:
                if (right - left + 1) < resultLen:
                    resultLen = right - left + 1
                    result = [left, right]
                leftChar = s[left]
                if leftChar in window:
                    window[leftChar] -= 1
                    if window[leftChar] < feqCount[leftChar]:
                        current -= 1
                left += 1

        return s[result[0]:result[1] + 1] if resultLen != float('inf') else ""


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
s = "a"
t = "a"
print(Solution().minWindow(s, t))
s = "a"
t = "aa"
print(Solution().minWindow(s, t))
