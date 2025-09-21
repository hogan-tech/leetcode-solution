# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def divideConquer(start: int, end: int) -> int:
            if end < k:
                return 0
            countMap = [0] * 26
            for i in range(start, end):
                countMap[ord(s[i]) - ord('a')] += 1

            for mid in range(start, end):
                if countMap[ord(s[mid]) - ord('a')] >= k:
                    continue
                midNext = mid + 1
                while midNext < end and countMap[ord(s[midNext]) - ord('a')] < k:
                    midNext += 1
                return max(divideConquer(start, mid), divideConquer(midNext, end))
            return end - start

        return divideConquer(0, len(s))


s = "aaabb"
k = 3
print(Solution().longestSubstring(s, k))
s = "ababbc"
k = 2
print(Solution().longestSubstring(s, k))
