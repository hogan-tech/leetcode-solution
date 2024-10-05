from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        freq1 = Counter(s1)
        freq2 = Counter(s2[0:n1])
        if freq1 == freq2:
            return True
        left = 1
        right = n1
        while right < n2:
            freq2[s2[left-1]] -= 1
            freq2[s2[right]] += 1
            if freq2 == freq1:
                return True
            left += 1
            right += 1

        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
