# time complexity: O(n^3)
# space complexity: O(n)
import re
from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        splitList = []
        result = [""]
        for splitString in re.split(r"[{}]", s):
            if splitString == "":
                continue
            if ',' in splitString:
                splitList.append(splitString.split(','))
            else:
                splitList.append(splitString)

        for splitString in splitList:
            if isinstance(splitString, list):
                originalListLen = len(result)
                result = list(result) * len(splitString)
                i = 0
                for c in splitString:
                    for _ in range(originalListLen):
                        result[i] += c
                        i += 1
            else:
                for i in range(len(result)):
                    result[i] += splitString

        result.sort()
        return result


'''
ac bc ac bc
[d, e]

'''
s = "{a,b}c{d,e}f"
print(Solution().expand(s))
s = "abcd"
print(Solution().expand(s))
