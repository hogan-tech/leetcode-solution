# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charIdx = {char: idx for idx, char in enumerate(order)}

        def customSort(char):
            return charIdx.get(char, float('inf'))
        sortedString = sorted(s, key=customSort)
        return "".join(sortedString)

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        result = []
        for c in order:
            if c in freq:
                result.append(c * freq[c])
                del freq[c]

        for c, count in freq.items():
            result.append((c * count))

        return ''.join(result)


order = "cba"
s = "abcd"
print(Solution().customSortString(order, s))
