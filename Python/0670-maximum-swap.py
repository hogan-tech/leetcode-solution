# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = list(str(num))
        n = len(numStr)
        maxRightIndex = [0] * n

        maxRightIndex[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            maxRightIndex[i] = (
                i
                if numStr[i] > numStr[maxRightIndex[i + 1]]
                else maxRightIndex[i + 1]
            )

        for i in range(n):
            if numStr[i] < numStr[maxRightIndex[i]]:
                numStr[i], numStr[maxRightIndex[i]] = (
                    numStr[maxRightIndex[i]],
                    numStr[i],
                )
                return int("".join(numStr))

        return num


num = 2736
print(Solution().maximumSwap(num))
