# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 3:
            n, remain = divmod(n, 3)
            if remain not in [0, 1]:
                return False
        if n not in [0, 1]:
            return False
        return True


n = 12
print(Solution().checkPowersOfThree(n))
n = 91
print(Solution().checkPowersOfThree(n))
n = 21
print(Solution().checkPowersOfThree(n))
