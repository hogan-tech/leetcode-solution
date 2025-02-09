# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        used = set()
        i = 1
        while len(used) < n:
            if k - i not in used:
                used.add(i)
            i += 1
        return sum(used)


n = 5
k = 4
print(Solution().minimumSum(n, k))
n = 2
k = 6
print(Solution().minimumSum(n, k))
