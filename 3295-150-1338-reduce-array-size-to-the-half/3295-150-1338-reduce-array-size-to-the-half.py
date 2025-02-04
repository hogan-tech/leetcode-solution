# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freqList = []
        for key, value in Counter(arr).items():
            freqList.append((value, key))
        freqList.sort(reverse=True)
        count = 0
        result = 0
        for i in range(len(freqList)):
            currCount, _ = freqList[i]
            count += currCount
            result += 1
            if count >= len(arr) // 2:
                return result
        return result


arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print(Solution().minSetSize(arr))
arr = [7, 7, 7, 7, 7, 7]
print(Solution().minSetSize(arr))
arr = []
print(Solution().minSetSize(arr))
