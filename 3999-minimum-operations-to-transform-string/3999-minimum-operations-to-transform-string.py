# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minOperations(self, s: str) -> int:
        result = 0
        for char in s:
            if char == 'a':
                continue
            diff = ord(char) - ord('a')
            ops = 26 - diff
            if ops > result:
                result = ops
        return result


s = "yz"
print(Solution().minOperations(s))
s = "a"
print(Solution().minOperations(s))
s = "abc"
print(Solution().minOperations(s))
s = "b"
print(Solution().minOperations(s))
