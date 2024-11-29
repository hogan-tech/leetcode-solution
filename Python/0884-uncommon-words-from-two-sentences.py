# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sList = list(s1.split(" ")) + list(s2.split(" "))
        result = []
        for item in Counter(sList).items():
            if item[1] == 1:
                result.append(item[0])
        return result


s1 = "this apple is sweet"
s2 = "this apple is sour"
print(Solution().uncommonFromSentences(s1, s2))
