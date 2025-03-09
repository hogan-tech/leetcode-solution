# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        left = 0
        right = 1
        result = 0
        while right < len(colors):
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
                continue
            right += 1
            if right - left < k:
                continue

            left += 1
            result += 1

        return result


colors = [0, 1, 0, 1, 0]
k = 3
print(Solution().numberOfAlternatingGroups(colors, k))
'''
  0 1 0 1 0|0 1 
T 0 1 0
T   1 0 1
T     0 1 0 
F       1 0 0
F         0 0 1
'''
colors = [0, 1, 0, 0, 1, 0, 1]
k = 6
print(Solution().numberOfAlternatingGroups(colors, k))
'''
  0 1 0 0 1 0 1|0 1 0 0 1
F 0 1 0 0 1 0      
F   1 0 0 1 0 1
F     0 0 1 0 1 0
T       0 1 0 1 0 1
T         1 0 1 0 1 0
F           0 1 0 1 0 0
F             1 0 1 0 0 1
'''
colors = [1, 1, 0, 1]
k = 4
print(Solution().numberOfAlternatingGroups(colors, k))
'''
  1 1 0 1|1 1 0
F 1 1 0 1
F   1 0 1 1
F     0 1 1 1
F       1 1 1 0
'''
