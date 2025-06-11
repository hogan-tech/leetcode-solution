# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(countA: int, countB: int) -> int:
            return ((countA & 1) << 1) | (countB & 1)

        n = len(s)
        result = float("-inf")
        for a in ["0", "1", "2", "3", "4"]:
            for b in ["0", "1", "2", "3", "4"]:
                if a == b:
                    continue

                best = [float("inf")] * 4
                countA = countB = 0
                prevA = prevB = 0
                left = -1
                for right in range(n):
                    countA += s[right] == a
                    countB += s[right] == b
                    while right - left >= k and countB - prevB >= 2:
                        leftStatus = getStatus(prevA, prevB)
                        best[leftStatus] = min(best[leftStatus], prevA - prevB)
                        left += 1
                        prevA += s[left] == a
                        prevB += s[left] == b

                    rightStatus = getStatus(countA, countB)
                    if best[rightStatus ^ 0b10] != float("inf"):
                        result = max(result, countA - countB -
                                     best[rightStatus ^ 0b10])

        return result


s = "12233"
k = 4
print(Solution().maxDifference(s, k))
s = "1122211"
k = 3
print(Solution().maxDifference(s, k))
