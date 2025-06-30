# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = []
        seen = set()
        currSeg = ""

        for c in s:
            currSeg += c
            if currSeg not in seen:
                seen.add(currSeg)
                segments.append(currSeg)
                currSeg = ""

        return segments


s = "abbccccd"
print(Solution().partitionString(s))
s = "aaaa"
print(Solution().partitionString(s))
