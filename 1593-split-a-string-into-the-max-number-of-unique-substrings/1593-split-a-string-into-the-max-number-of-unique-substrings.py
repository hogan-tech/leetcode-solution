# time complexity: O(n* 2^n)
# space complexity: O(n)
class Solution:
    def backtrack(self, s: str, start: int, seen: set) -> int:
        if start == len(s):
            return 0

        maxCount = 0
        for end in range(start + 1, len(s) + 1):
            subString = s[start:end]
            if subString not in seen:
                seen.add(subString)
                maxCount = max(maxCount, 1 + self.backtrack(s, end, seen))
                seen.remove(subString)

        return maxCount

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s, 0, seen)


s = "ababccc"
print(Solution().maxUniqueSplit(s))
