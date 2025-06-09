# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {c: i for i, c in enumerate(s)}

        partitionEnd = 0
        partitionStart = 0
        partitionSize = []

        for i, c in enumerate(s):
            partitionEnd = max(partitionEnd, lastIdx[c])
            if i == partitionEnd:
                partitionSize.append(partitionEnd - partitionStart + 1)
                partitionStart = partitionEnd + 1

        return partitionSize


'''
ababcbacadefegdehijhklij
{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11,
    'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}

5 == 5 
result.append

'''
s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))
s = "eccbbbbdec"
print(Solution().partitionLabels(s))
