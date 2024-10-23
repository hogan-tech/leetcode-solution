# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def convertString(self, string: str):
        temp = ""
        diff = ord(string[0]) - ord('a')
        for c in string:
            alphet = ord(c) - diff
            temp += chr(alphet + 26 if alphet < ord('a') else alphet)
        return temp

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)
        for string in strings:
            if string[0] == 'a':
                groupDict[string].append(string)
            else:
                groupDict[self.convertString(string)].append(string)
        result = []
        for value in groupDict.values():
            result.append(value)
        return result


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(Solution().groupStrings(strings))
