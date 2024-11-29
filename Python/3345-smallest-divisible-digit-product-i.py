# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(x):
            product = 1
            for digit in str(x):
                product *= int(digit)
            return product

        while True:
            if digitProduct(n) % t == 0:
                return n
            n += 1


n = 15
t = 2
print(Solution().smallestNumber(n, t))
