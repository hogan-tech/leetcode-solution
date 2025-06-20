# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        fourDirs = ['NE', 'NW', 'SE', 'SW']
        result = 0
        for currDir in fourDirs:
            currCount = 0
            remainK = k
            for i in range(len(s)):
                if s[i] in currDir:
                    currCount += 1
                else:
                    if remainK:
                        remainK -= 1
                        currCount += 1
                    else:
                        currCount -= 1
                result = max(result, currCount)
        return result


s = "NWSE"
k = 1
print(Solution().maxDistance(s, k))
s = "NSWWEW"
k = 3
print(Solution().maxDistance(s, k))
