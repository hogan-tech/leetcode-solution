from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        results = [""]
        best = 0
        for word in arr:
            for i in range(len(results)):
                newRes = results[i] + word
                if len(newRes) != len(set(newRes)):
                    continue
                results.append(newRes)
                best = max(best, len(newRes))
        return best


arr = ["un", "iq", "ue"]
print(Solution().maxLength(arr))
