from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]] * len(pref)
        for i in range(1, len(pref)):
            ans[i] = pref[i-1] ^ pref[i]
        return ans


pref = [5, 2, 0, 3, 1]
print(Solution().findArray(pref))
