# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        prev = ""
        for c in s:
            if c in prev:
                prev = c
                count += 1
            else:
                prev += c
        return count


s = "abacaba"
print(Solution().partitionString(s))
s = "ssssss"
print(Solution().partitionString(s))
s = "hdklqkcssgxlvehva"
print(Solution().partitionString(s))
