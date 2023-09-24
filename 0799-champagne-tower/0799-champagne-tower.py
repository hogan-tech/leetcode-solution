class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        Arr = [[0] * k for k in range(1, 102)]
        Arr[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (Arr[r][c] - 1.0)/2.0
                if q > 0:
                    Arr[r + 1][c] += q
                    Arr[r + 1][c+1] += q
        return min(1, Arr[query_row][query_glass])


poured = 2
query_row = 1
query_glass = 1

print(Solution().champagneTower(poured, query_row, query_glass))
