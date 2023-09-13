from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        SumAlice, SumBob = sum(aliceSizes), sum(bobSizes)
        setB = set(bobSizes)
        for item in aliceSizes:
            if item + (SumBob - SumAlice) // 2 in setB:
                return [item, item + (SumBob - SumAlice) // 2]


aliceSizes = [1, 1]
bobSizes = [2, 2]


print(Solution().fairCandySwap(aliceSizes, bobSizes))
