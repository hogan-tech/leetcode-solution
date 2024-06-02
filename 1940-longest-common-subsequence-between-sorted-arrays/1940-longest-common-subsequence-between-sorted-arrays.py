# time complexity: O(m*n)
# space complexity: O(m*n)
from collections import defaultdict
from typing import List


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        freqArr = defaultdict(int)
        result = []
        for array in arrays:
            for num in array:
                freqArr[num] += 1
                if freqArr[num] == len(arrays):
                    result.append(num)

        return result


arrays = [[1, 3, 4],
          [1, 4, 7, 9]]
print(Solution().longestCommonSubsequence(arrays))
