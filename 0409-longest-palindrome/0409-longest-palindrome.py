class Solution:
    def longestPalindrome(self, s: str) -> int:
        pair = 0
        unpair_set = set()

        for c in s:
            if c in unpair_set:
                unpair_set.remove(c)
                pair += 1
            else:
                unpair_set.add(c)

        return 2 * pair + 1 if unpair_set else 2 * pair