# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        original = [i for i in range(n)]
        perm = list(original)
        arr = [0 for _ in range(n)]
        count = 0
        while list(arr) != list(original):
            for i in range(n):
                if i % 2:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
                else:
                    arr[i] = perm[i // 2]
            perm = list(arr)
            count += 1
            if list(arr) == list(original):
                break
            arr = [0 for _ in range(n)]
        return count


n = 2
print(Solution().reinitializePermutation(n))
n = 4
print(Solution().reinitializePermutation(n))
n = 6
print(Solution().reinitializePermutation(n))
