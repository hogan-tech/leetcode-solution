# time complexity: O(sqrt(n) log * log sqrt(n))
# space complexity: O(sqrt(n))
from math import sqrt


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        TOTAL = int(sqrt(r))
        prime = [False, False] + [True] * (TOTAL - 1)
        for i in range(2, int(sqrt(TOTAL)) + 1):
            if prime[i]:
                for j in range(i * 2, TOTAL + 1, i):
                    prime[j] = False

        count = 0
        for i in range(2, TOTAL + 1):
            if prime[i]:
                square = i ** 2
                if l <= square <= r:
                    count += 1

        return r - l + 1 - count


'''
prime is not
 4 -> 2
 9 -> 3
25 -> 5
49 -> 7

4 <- 5, 6, 7 <- 9

prime * 2
02
03
04 = 2
05 = 
06 = 2, 3
07 = 
08 = 2, 4
09 = 3
010 = 2, 5
11 = 
12 = 
13 = 
14 = 
15 = 
16 = 
'''

l = 5
r = 7
print(Solution().nonSpecialCount(l, r))
l = 4
r = 16
print(Solution().nonSpecialCount(l, r))
