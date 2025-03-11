# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        aIdx = -1
        bIdx = -1
        cIdx = -1
        for i, c in enumerate(s):
            if c == 'a':
                aIdx = i
            if c == 'b':
                bIdx = i
            if c == 'c':
                cIdx = i
            if aIdx >= 0 and bIdx >= 0 and cIdx >= 0:
                left = min(aIdx, bIdx, cIdx)
                result += left + 1

        return result


'''
a b a b b b c a
0 0 0 0 0 0 3 6
    l       r
            e
'''
s = "ababbbca"
print(Solution().numberOfSubstrings(s))
'''
a b c a b c
0 0 1 2 3 4
l   r     e 
'''
s = "abcabc"
print(Solution().numberOfSubstrings(s))
'''
a a a c b
0 0 0 0 3
    l   r
        e
'''
s = "aaacb"
print(Solution().numberOfSubstrings(s))
'''
a b c
0 0 1
l   r
    e
'''
s = "abc"
print(Solution().numberOfSubstrings(s))
'''
b c b c c b a
0 0 0 0 0 0 5
            s
            e
'''
s = 'bcbccba'
print(Solution().numberOfSubstrings(s))
