# time complexity: O(n)
# space complexity: O(k)
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {c: i for i, c in enumerate(s)}
        right = 0
        left = 0
        result = []
        for i, c in enumerate(s):
            right = max(right, lastIdx[c])
            if i == right:
                result.append(right - left + 1)
                left = right + 1
        return result

# time complexity: O(n)
# space complexity: O(k)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        lastIdx = [0] * 26
        firstIdx = [-1] * 26
        left, right = 0, 0
        for i, char in enumerate(s):
            lastIdx[ord(char) - ord("a")] = i
        for i, char in enumerate(s):
            index = ord(char) - ord("a")
            if firstIdx[index] == -1:
                firstIdx[index] = i
            if right < firstIdx[index]:
                result.append(right - left + 1)
                left = i
                right = i
            right = max(right, lastIdx[index])
        if right - left + 1 > 0:
            result.append(right - left + 1)

        return result


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
