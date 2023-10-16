from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)

        def calculateSum(l, r):
            cnt = min(books[r], r - l + 1)
            return (2 * books[r] - (cnt - 1)) * cnt // 2

        stack = []
        dp = [0] * n

        for i in range(n):
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calculateSum(j + 1, i)

            stack.append(i)

        return max(dp)


books = [8, 5, 2, 7, 9]

print(Solution().maximumBooks(books))
