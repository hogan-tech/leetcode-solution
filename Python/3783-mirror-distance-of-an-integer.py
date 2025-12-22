# time complexity: O(1)
# space complexity: O(n)
class Solution:
    def mirrorDistance(self, n: int) -> int:
        num = str(n)
        reverseNum = num[::-1]
        return abs(int(num) - int(reverseNum))


n = 25
print(Solution().mirrorDistance(n))
n = 10
print(Solution().mirrorDistance(n))
n = 7
print(Solution().mirrorDistance(n))
