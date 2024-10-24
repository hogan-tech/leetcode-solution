from collections import Counter, defaultdict
from functools import lru_cache


class Solution:
    def RLE(self, countString: str):
        temp = ""
        freqDict = defaultdict(int)
        freqDict[countString[0]] += 1
        for i in range(1,len(countString)):
            if countString[i] != countString[i-1]:
                key = countString[i-1]
                freq = freqDict[countString[i-1]]
                temp += str(freq) + key
                del freqDict[countString[i-1]]
                freqDict[countString[i]] += 1
            else:
                freqDict[countString[i]] += 1
        for key, freq in freqDict.items():
            temp += str(freq) + key
        return temp

    @lru_cache(None)
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.RLE(self.countAndSay(n-1))


n = 4
print(Solution().countAndSay(n))
