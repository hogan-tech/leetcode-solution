class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        SList, TList = list(sorted(s)), list(sorted(t))
        for i in range(len(SList)):
            if(SList[i] != TList[i]):
                return TList[i]
        return TList[-1]
    

s = "abcd"
t = "abcde"

print(Solution().findTheDifference(s,t))