# time complextiy: O(n)
# space complexity: O(1)
class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            if bin(n).count('0') == 1:
                return n
            n += 1


n = 5
print(Solution().smallestNumber(n))
n = 10
print(Solution().smallestNumber(n))
n = 3
print(Solution().smallestNumber(n))
