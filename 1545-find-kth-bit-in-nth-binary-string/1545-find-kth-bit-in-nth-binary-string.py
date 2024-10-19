class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        memo = ["0"] * (n + 1)
        memoInvert = ["1"] * (n + 1)
        for i in range(1, n+1):
            memo[i] = memo[i-1] + "1" + memoInvert[i-1][::-1]
            memoInvert[i] = ''.join(['1' if j == '0' else '0'
                                     for j in memo[i]])
        return memo[n][k-1]


n = 3
k = 1
print(Solution().findKthBit(n, k))
