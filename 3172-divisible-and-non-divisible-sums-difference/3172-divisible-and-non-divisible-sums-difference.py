# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = []
        notDivisible = []
        for i in range(1, n + 1):
            if i % m == 0:
                divisible.append(i)
            else:
                notDivisible.append(i)

        return sum(notDivisible) - sum(divisible)


n = 10
m = 3
print(Solution().differenceOfSums(n, m))
n = 5
m = 6
print(Solution().differenceOfSums(n, m))
n = 5
m = 1
print(Solution().differenceOfSums(n, m))
