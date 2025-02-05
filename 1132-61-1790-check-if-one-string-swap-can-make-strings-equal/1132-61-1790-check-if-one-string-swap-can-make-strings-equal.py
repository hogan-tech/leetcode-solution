# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        if Counter(s1) != Counter(s2):
            return False
        return count == 2 or count == 0


s1 = "bank"
s2 = "kanb"
print(Solution().areAlmostEqual(s1, s2))
s1 = "attack"
s2 = "defend"
print(Solution().areAlmostEqual(s1, s2))
s1 = "kelb"
s2 = "kelb"
print(Solution().areAlmostEqual(s1, s2))
s1 = "siyolsdcjthwsiplccjbuceoxmpjgrauocx"
s2 = "siyolsdcjthwsiplccpbuceoxmjjgrauocx"
print(Solution().areAlmostEqual(s1, s2))
s1 = "caa"
s2 = "aca"
print(Solution().areAlmostEqual(s1, s2))
