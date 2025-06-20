# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        counter1 = Counter(s1)
        counter2 = Counter(s2[:n1])
        if counter1 == counter2:
            return True
        for i in range(n2 - n1 ):
            leftChar = s2[i]
            rightChar = s2[i + n1]
            counter2[leftChar] -= 1
            counter2[rightChar] += 1
            if counter1 == counter2:
                return True

        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2))
s1 = "adc"
s2 = "dcda"
print(Solution().checkInclusion(s1, s2))
