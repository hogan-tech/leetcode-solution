# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign

'''
x = 15
y = 2

0 1 1 1 1
0 0 0 1 0

x^y = answer
0 1 1 0 1

(x & y) << 1 = carry
0 0 1 0 0

if x & y same sign
1. 
0 1 1 1 1
0 0 0 1 0
2. 
0 1 1 0 1
0 0 1 0 0
3.
0 1 0 0 1
0 1 0 0 0
4.
0 0 0 0 1
1 0 0 0 0
5.
1 0 0 0 1 -> 16
0 0 0 0 0


if x & y diff sign

x = 15, y = 2, ~x = -16

0 1 1 1 1
1 0 0 0 0
0 0 0 1 0

0 1 1 0 1
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        maxInt = 0x7FFFFFFF
        return a if a < maxInt else ~(a ^ mask)
    
a = 1
b = 2
print(Solution().getSum(a, b))
a = 2
b = 3
print(Solution().getSum(a, b))
