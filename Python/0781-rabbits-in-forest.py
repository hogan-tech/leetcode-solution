# time complexity: O(n)
# space complexity: O(n)
import math
from typing import Counter, List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        result = 0
        for key, val in counter.items():
            result += ((key + 1) * math.ceil(val / (key + 1)))
        return result


'''
(key + 1) * ceil(val / (key + 1))
0: 1 -> a
0: 2 -> a b
0: 3 -> a b c

(key + 1) * ceil(val / (key + 1))
1: 1 -> a a
1: 2 -> a a
1: 3 -> a a b b
1: 4 -> a a b b

(key + 1) * ceil(val / (key + 1))
2: 1 -> b b b
2: 2 -> b b b
2: 3 -> b b b
2: 4 -> b b b c c c
2: 5 -> b b b c c c
2: 6 -> b b b c c c
2: 7 -> b b b c c c d d d
'''
answers = [1, 1, 1, 0, 0]
print(Solution().numRabbits(answers))
answers = [1, 1, 2]
print(Solution().numRabbits(answers))
answers = [10, 10, 10]
print(Solution().numRabbits(answers))
