import re


class Solution:
    def removeVowels(self, s: str) -> str:
        return re.sub(r'[aeiou]', '', s)


s = "leetcodeisacommunityforcoders"
print(Solution().removeVowels(s))
