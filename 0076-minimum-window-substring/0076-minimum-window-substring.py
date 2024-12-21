# time complexity: O(len(s) + len(t))
# space complexity: O(len(s) + len(t))
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        reqCount = defaultdict(int)
        window = defaultdict(int)
        result = [-1, -1]
        resultLen = float('inf')
        current = 0
        

        for char in t:
            reqCount[char] += 1

        required = len(reqCount)

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in reqCount:
                window[char] += 1
                if window[char] == reqCount[char]:
                    current += 1
            while current == required:
                if (right - left + 1) < resultLen:
                    resultLen = right - left + 1
                    result = [left, right]
                leftChar = s[left]
                if leftChar in window:
                    window[leftChar] -= 1
                    if window[leftChar] < reqCount[leftChar]:
                        current -= 1
                left += 1

        return s[result[0]:result[1] + 1] if resultLen != float('inf') else ""
        


S = "ADOBECODEBANC"
T = "ABC"


print(Solution().minWindow(S, T))
