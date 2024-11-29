from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for item in intervals:
            if merged[-1][1] < item[0]:
                merged.append(item)
            else:
                merged[-1][1] = max(merged[-1][1], item[1])
        return merged