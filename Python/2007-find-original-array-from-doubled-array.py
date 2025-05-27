# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        result = []
        changed.sort()
        freq = defaultdict(int)
        for num in changed:
            freq[num] += 1

        for num in changed:
            if freq[num]:
                freq[num] -= 1
                doubleNum = num * 2
                if freq[doubleNum] > 0:
                    freq[doubleNum] -= 1
                    result.append(num)
                else:
                    return []
        return result


changed = [1, 3, 4, 2, 6, 8]
print(Solution().findOriginalArray(changed))
changed = [6, 3, 0, 1]
print(Solution().findOriginalArray(changed))
changed = [1]
print(Solution().findOriginalArray(changed))
changed = [0, 0, 0, 0]
print(Solution().findOriginalArray(changed))
