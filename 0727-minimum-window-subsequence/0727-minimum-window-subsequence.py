# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        minSubsequence = ""
        minSubLength = float('inf')
        sizeS1 = len(s1)
        sizeS2 = len(s2)
        idxS1 = 0
        idxS2 = 0
        while idxS1 < sizeS1:
            if s1[idxS1] == s2[idxS2]:
                idxS2 += 1
                if idxS2 == sizeS2:
                    start = idxS1
                    end = idxS1
                    idxS2 -= 1
                    while idxS2 >= 0:
                        if s2[idxS2] == s1[start]:
                            idxS2 -= 1
                        start -= 1
                    start += 1
                    currLength = end - start
                    if currLength < minSubLength:
                        minSubLength = currLength
                        minSubsequence = s1[start:end+1]
                    idxS1 = start
            idxS1 += 1

        return minSubsequence


s1 = "abcdebdde"
s2 = "bde"
print(Solution().minWindow(s1, s2))
s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
s2 = "u"
print(Solution().minWindow(s1, s2))
