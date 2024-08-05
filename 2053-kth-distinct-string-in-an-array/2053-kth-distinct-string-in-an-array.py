from typing import Counter, List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinctList = []
        for item in Counter(arr).items():
            if item[1] == 1:
                distinctList.append(item[0])
        return distinctList[k-1] if k-1 < len(distinctList) else ""


arr = ["d", "b", "c", "b", "c", "a"]
k = 2
print(Solution().kthDistinct(arr, k))
