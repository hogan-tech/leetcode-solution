# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 0
        for c in s:
            if c in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
        if vowels == 0:
            return False
        return True


'''
case odd
Alice win

case even 0
Alice lose

case even > 2
get until last vowel - 1
Alice Win

case even > 2
but last vowel is contigious
Alice lose
'''
s = "leetcoder"
print(Solution().doesAliceWin(s))
s = "bbcd"
print(Solution().doesAliceWin(s))
