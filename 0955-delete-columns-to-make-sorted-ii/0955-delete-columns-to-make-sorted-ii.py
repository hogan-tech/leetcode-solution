# time complexity: O(n * w^2)
# space complexity: O(n * w)
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def isSorted(strs):
            return all(strs[i] <= strs[i+1] for i in range(len(strs) - 1))
        result = 0
        curr = [""] * len(strs)

        for col in zip(*strs):
            curr2 = curr[:]
            for i, letter in enumerate(col):
                curr2[i] = curr2[i] + letter
            if isSorted(curr2):
                curr = curr2
            else:
                result += 1
                
        return result


strs = ["ca", "bb", "ac"]
print(Solution().minDeletionSize(strs))
strs = ["xc", "yb", "za"]
print(Solution().minDeletionSize(strs))
strs = ["zyx", "wvu", "tsr"]
print(Solution().minDeletionSize(strs))
