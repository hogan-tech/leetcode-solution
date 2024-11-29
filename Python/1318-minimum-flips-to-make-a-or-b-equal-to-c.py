# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aBin = bin(a)[2:]
        bBin = bin(b)[2:]
        cBin = bin(c)[2:]

        maxLen = max(len(aBin), len(bBin), len(cBin))

        aBin = aBin.zfill(maxLen)
        bBin = bBin.zfill(maxLen)
        cBin = cBin.zfill(maxLen)

        ans = 0
        for i in range(maxLen):
            if cBin[i] == '0':
                if aBin[i] == '1' and bBin[i] == '1':
                    ans += 2
                elif aBin[i] == '1' or bBin[i] == '1':
                    ans += 1
            elif cBin[i] == "1":
                if aBin[i] == '0' and bBin[i] == '0':
                    ans += 1
        return ans


a = 2
b = 6
c = 5
print(Solution().minFlips(a, b, c))
