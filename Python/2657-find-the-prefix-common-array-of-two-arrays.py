# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        numSet = set()
        count = 0
        result = []
        for i in range(len(A)):
            if A[i] not in numSet:
                numSet.add(A[i])
            else:
                count += 1
            if B[i] not in numSet:
                numSet.add(B[i])
            else:
                count += 1
            result.append(count)

        return result


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
print(Solution().findThePrefixCommonArray(A, B))
A = [2, 3, 1]
B = [3, 1, 2]
print(Solution().findThePrefixCommonArray(A, B))
