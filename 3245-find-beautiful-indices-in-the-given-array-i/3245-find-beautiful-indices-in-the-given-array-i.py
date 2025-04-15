# time complexity: O(nlogn)
# space complexity: O(n)
import bisect
from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        aList, bList = [], []
        n, aLen, bLen = len(s), len(a), len(b)

        for i in range(n-aLen+1):
            if s[i:i+aLen] == a:
                aList.append(i)
        for i in range(n-bLen+1):
            if s[i:i+bLen] == b:
                bList.append(i)

        if not aList or not bList:
            return []

        result = []
        for i in aList:
            idx = bisect.bisect_left(bList, i)
            if idx == 0:
                if abs(i-bList[idx]) <= k:
                    result.append(i)

            elif idx == len(bList):
                if abs(i-bList[idx-1]) <= k:
                    result.append(i)

            else:
                v1 = bList[idx]
                v2 = bList[idx-1]
                if abs(i-v1) <= k or abs(i-v2) <= k:
                    result.append(i)

        return result


'''

abs(j - i) <= k
-k <= j - i <= k
-k + i <= j <= k + i
leftBound <= j <= rightBound

-15 + 16 <= j <= 15 + 16
1 <= j <= 31
'''

s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15
print(Solution().beautifulIndices(s, a, b, k))
s = "abcd"
a = "a"
b = "a"
k = 4
print(Solution().beautifulIndices(s, a, b, k))
