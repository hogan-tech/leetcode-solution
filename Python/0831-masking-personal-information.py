# time complexity: O(n)
# space complexity: O(n)
import re


class Solution:
    def maskPII(self, s: str) -> str:
        if s[-1].isalpha():
            charList = re.split(r'[@.]', s)
            charList[0] = charList[0].lower()
            charList[0] = charList[0][0] + "*" * 5 + charList[0][-1]
            charList[1] = charList[1].lower()
            return charList[0] + "@" + charList[1] + "." + charList[2].lower()
        else:
            numList = []
            for c in s:
                if c.isdigit():
                    numList.append(c)

            if len(numList) == 10:
                return "***-***-" + ''.join(numList[6:11])
            if len(numList) == 11:
                return "+*-***-***-" + ''.join(numList[7:12])
            if len(numList) == 12:
                return "+**-***-***-" + ''.join(numList[8:13])
            if len(numList) == 13:
                return "+***-***-***-" + ''.join(numList[9:14])


s = "LeetCode@LeetCode.com"
print(Solution().maskPII(s))
s = "AB@qq.com"
print(Solution().maskPII(s))
s = "1(234)567-890"
print(Solution().maskPII(s))
