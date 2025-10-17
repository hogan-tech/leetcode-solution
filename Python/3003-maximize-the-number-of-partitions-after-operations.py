# time complexity: O(m * n) m = 26
# space complexity: O(n)
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]

        num, mask, count = 0, 0, 0
        for i in range(n - 1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            left[i + 1][0] = num
            left[i + 1][1] = mask
            left[i + 1][2] = count

        num, mask, count = 0, 0, 0
        for i in range(n - 1, 0, -1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            right[i - 1][0] = num
            right[i - 1][1] = mask
            right[i - 1][2] = count

        maxValue = 0
        for i in range(n):
            segment = left[i][0] + right[i][0] + 2
            totalMask = left[i][1] | right[i][1]
            totalCount = bin(totalMask).count("1")
            if left[i][2] == k and right[i][2] == k and totalCount < 26:
                segment += 1
            elif min(totalCount + 1, 26) <= k:
                segment -= 1
            maxValue = max(maxValue, segment)
        return maxValue


s = "accca"
k = 2
print(Solution().maxPartitionsAfterOperations(s, k))
s = "aabaab"
k = 3
print(Solution().maxPartitionsAfterOperations(s, k))
s = "xxyz"
k = 1
print(Solution().maxPartitionsAfterOperations(s, k))
