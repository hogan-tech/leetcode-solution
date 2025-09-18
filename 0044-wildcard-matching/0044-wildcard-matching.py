# time complexity: O(s * p * (s + p))
# space complexity: O(s * p)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def removeDuplicateStarts(p: str) -> str:
            newString = []
            for char in p:
                if not newString or char != "*":
                    newString.append(char)
                elif newString[-1] != "*":
                    newString.append(char)
            return "".join(newString)

        def helper(s: str, p: str) -> bool:
            if (s, p) in dp:
                return dp[(s, p)]
            if p == s or p == "*":
                dp[(s, p)] = True
            elif p == "" or s == "":
                dp[(s, p)] = False
            elif p[0] == s[0] or p[0] == "?":
                dp[(s, p)] = helper(s[1:], p[1:])
            elif p[0] == "*":
                dp[(s, p)] = helper(s, p[1:]) or helper(s[1:], p)
            else:
                dp[(s, p)] = False
            return dp[(s, p)]
        dp = {}
        p = removeDuplicateStarts(p)
        return helper(s, p)

# time complexity: O(s * p)
# space complexity: O(s * p)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen = len(s)
        pLen = len(p)
        if p == s or set(p) == {"*"}:
            return True
        if p == "" or s == "":
            return False
        d = [[False for _ in range(sLen + 1)] for _ in range(pLen + 1)]
        d[0][0] = True
        for pIdx in range(1, pLen + 1):
            if p[pIdx - 1] == "*":
                sIdx = 1
                while not d[pIdx - 1][sIdx - 1] and sIdx < sLen + 1:
                    sIdx += 1
                d[pIdx][sIdx - 1] = d[pIdx - 1][sIdx - 1]
                while sIdx < sLen + 1:
                    d[pIdx][sIdx] = True
                    sIdx += 1
            elif p[pIdx - 1] == "?":
                for sIdx in range(1, sLen + 1):
                    d[pIdx][sIdx] = d[pIdx - 1][sIdx - 1]
            else:
                for sIdx in range(1, sLen + 1):
                    d[pIdx][sIdx] = (d[pIdx - 1][sIdx - 1]
                                     and p[pIdx - 1] == s[sIdx - 1])
        return d[pLen][sLen]

# time complexity: O(min(s, p))
# space complexity: O(1)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)
        sIdx = pIdx = 0
        starIdx = sTempIdx = -1

        while sIdx < sLen:
            if pIdx < pLen and p[pIdx] in ["?", s[sIdx]]:
                sIdx += 1
                pIdx += 1

            elif pIdx < pLen and p[pIdx] == "*":
                starIdx = pIdx
                sTempIdx = sIdx
                pIdx += 1

            elif starIdx == -1:
                return False

            else:
                pIdx = starIdx + 1
                sIdx = sTempIdx + 1
                sTempIdx = sIdx

        return all(p[i] == "*" for i in range(pIdx, pLen))
    
s = "aa"
p = "a"
print(Solution().isMatch(s, p))
s = "aa"
p = "*"
print(Solution().isMatch(s, p))
s = "cb"
p = "?a"
print(Solution().isMatch(s, p))
