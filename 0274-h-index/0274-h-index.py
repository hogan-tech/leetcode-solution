# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hIdx = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                hIdx += 1
        return hIdx


citations = [3, 0, 6, 1, 5]
print(Solution().hIndex(citations))
