# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        return abs(s.count('b') - s.count('a'))


s = "aabbab"
print(Solution().minLengthAfterRemovals(s))
s = "aaaa"
print(Solution().minLengthAfterRemovals(s))
s = "aaabb"
print(Solution().minLengthAfterRemovals(s))
