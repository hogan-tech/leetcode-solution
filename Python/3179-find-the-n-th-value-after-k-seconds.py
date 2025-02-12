# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ROW = k + 1
        COL = n
        grid = [[0 for _ in range(COL)]for _ in range(ROW)]
        for r in range(ROW):
            grid[r][0] = 1
        for c in range(COL):
            grid[0][c] = 1
        for r in range(1, ROW):
            for c in range(1, COL):
                grid[r][c] = (grid[r - 1][c] + grid[r][c-1]) % MOD
        return grid[r][c]


'''
0	[1,1,1,1]
1	[1,2,3,4]
2	[1,3,6,10]
3	[1,4,10,20]
4	[1,5,15,35]
5	[1,6,21,56]
'''
n = 4
k = 5
print(Solution().valueAfterKSeconds(n, k))
n = 5
k = 3
print(Solution().valueAfterKSeconds(n, k))
