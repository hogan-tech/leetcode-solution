# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        counter = defaultdict(list)
        arrList = list(s)
        for i, c in enumerate(arrList):
            if c != '*':
                counter[ord(c) - ord('a')].append(i)
            else:
                for j in range(26):
                    if counter[j]:
                        arrList[counter[j].pop()] = '*'
                        break
        return "".join(c for c in arrList if c != '*')


s = "aaba*"
print(Solution().clearStars(s))
s = "abc"
print(Solution().clearStars(s))
