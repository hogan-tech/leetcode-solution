# time complexity: O(k)
# space complexity: O(1)
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for num in range(1, k+1):
            remainder = (remainder*10+1) % k
            if remainder == 0:
                return num
        return -1


k = 1
print(Solution().smallestRepunitDivByK(k))
k = 2
print(Solution().smallestRepunitDivByK(k))
k = 3
print(Solution().smallestRepunitDivByK(k))
k = 7
print(Solution().smallestRepunitDivByK(k))
k = 70
print(Solution().smallestRepunitDivByK(k))
