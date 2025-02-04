# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0 for _ in range(n)]
        for i in range(n):
            arr[i] = (2 * i) + 1
        mid = (arr[0] + arr[n - 1]) // 2
        result = 0
        for i in range(n // 2):
            result += mid - arr[i]
        return result


n = 3
print(Solution().minOperations(n))
n = 6
print(Solution().minOperations(n))
