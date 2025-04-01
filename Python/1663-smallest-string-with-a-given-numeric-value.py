# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        rightCount = (k - n) // 25
        mid = (k - n) % 25
        midChar = chr(mid + ord('a')) if rightCount != n else ""
        leftCount = n - rightCount - 1 if rightCount != n else n - rightCount
        return "a" * leftCount + midChar + "z" * rightCount


n = 3
k = 27
print(Solution().getSmallestString(n, k))
n = 5
k = 73
print(Solution().getSmallestString(n, k))
n = 5
k = 130
print(Solution().getSmallestString(n, k))
