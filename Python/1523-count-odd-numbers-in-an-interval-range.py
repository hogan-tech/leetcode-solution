class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1
    
'''
even even
10 16 -> 11 13 15 -> (16 - 10) // 2

odd even
11 16 -> 11 13 15 -> (16 - 11) // 2 + 1

odd odd
11 15 -> 11 13 15 -> (15 - 11) // 2 + 1

even odd
10 15 -> 11 13 15 -> (15 - 10) // 2 + 1
'''


low = 3
high = 7
print(Solution().countOdds(low, high))
low = 8
high = 10
print(Solution().countOdds(low, high))
