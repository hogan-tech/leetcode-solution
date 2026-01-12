class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        maxArea = 0
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == '1':
                    width = dp[r][c] = dp[r][c-1] + 1 if c else 1
                    for h in range(r, -1, -1):
                        width = min(width, dp[h][c])
                        maxArea = max(maxArea, width * (r - h + 1))
        return maxArea