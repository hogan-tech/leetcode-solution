# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        blackCount = 0
        for char in s:
            if char == "0":
                swaps += blackCount
            else:
                blackCount += 1
        return swaps


s = "0111"
print(Solution().minimumSteps(s))
