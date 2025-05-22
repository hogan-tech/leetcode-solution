# time complexity: O(logn)
# space complexity: O(1)
from collections import deque
from math import log
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(log(label, 2))
        result = deque()
        for currLevel in range(level, -1, -1):
            result.appendleft(label)
            firstNode = 2 ** currLevel
            lastNode = 2 ** (currLevel + 1) - 1
            label = (firstNode + lastNode - label) // 2

        return list(result)


'''
0            1 
1      3          2
2   4     5     6    7
3 15 14 13 12 11 10 9 8

(23 - 14) // 2

13 -> 5 -> 3 -> 1
14 -> 4 -> 3 -> 1


0            1 
1      2            3
2   4     5      6      7
3 8  9  10  11 12 13  14 15

14 -> 7 -> 3 -> 1
13 -> 6 -> 3 -> 1
11 -> 5 -> 2 -> 1
'''


label = 14
print(Solution().pathInZigZagTree(label))
label = 26
print(Solution().pathInZigZagTree(label))
