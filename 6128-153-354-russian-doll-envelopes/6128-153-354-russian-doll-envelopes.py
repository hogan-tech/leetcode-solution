# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def binarySearch(arr: List[int], target: int):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        longestIncreasingSub = []
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        for _, height in envelopes:
            position = binarySearch(longestIncreasingSub, height)
            if position == len(longestIncreasingSub):
                longestIncreasingSub.append(height)
            else:
                longestIncreasingSub[position] = height
        return len(longestIncreasingSub)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(envelopes))
envelopes = [[1, 1], [1, 1], [1, 1]]
print(Solution().maxEnvelopes(envelopes))
