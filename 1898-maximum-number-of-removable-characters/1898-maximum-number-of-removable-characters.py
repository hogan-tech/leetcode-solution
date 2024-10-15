# time complexity: O(mlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        count = 0
        left, right = 0, len(removable)

        def isSeq(idx: int):
            remove = {removable[i] for i in range(idx)}
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i not in remove:
                    if s[i] == p[j]:
                        j += 1
                i += 1
            return j == len(p)

        while left <= right:
            mid = (left+right)//2
            if isSeq(mid):
                count = mid
                left = mid + 1
            else:
                right = mid - 1
        return count


s = "abcacb"
p = "ab"
removable = [3, 1, 0]
print(Solution().maximumRemovals(s, p, removable))
