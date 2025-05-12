# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        freq.sort(reverse=True)
        return sum(freq[k:])


s = "abc"
k = 2
print(Solution().minDeletion(s, k))
s = "aabb"
k = 2
print(Solution().minDeletion(s, k))
s = "yyyzz"
k = 1
print(Solution().minDeletion(s, k))
