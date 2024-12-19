# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        start = 0
        end = len(s) - 1
        moves = 0
        while start < end:
            curr = end
            while curr > start:
                if s[start] == s[curr]:
                    for temp in range(curr, end):
                        s[temp], s[temp + 1] = s[temp + 1], s[temp]
                        moves += 1
                    end -= 1
                    break
                curr -= 1
            if curr == start:
                moves += len(s) // 2 - start
            start += 1
        return moves


s = "aabb"
print(Solution().minMovesToMakePalindrome(s))
s = "letelt"
print(Solution().minMovesToMakePalindrome(s))
