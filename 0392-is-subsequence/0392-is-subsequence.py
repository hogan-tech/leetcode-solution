class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sList, tList = list(s), list(t)
        acc = 0
        if s == "":
            return True
        for item in tList:
            if acc == len(sList):
                return True
            if (item == sList[acc]):
                acc += 1
        return True if acc == len(sList) else False


s = "b"
t = "abc"

print(Solution().isSubsequence(s, t))
