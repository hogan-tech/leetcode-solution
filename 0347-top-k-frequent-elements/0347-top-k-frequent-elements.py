from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        MostCommon = Counter(nums).most_common(k)
        for item, count in MostCommon:
            result.append(item)
        return result