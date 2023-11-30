# time complexity: O(log^2 n)
# space complexity: O(logn)
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        k = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            k += 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)


n = 3
print(Solution)
