# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        minSubsequence = ""
        minSubLength = float('inf')
        l1 = len(s1)
        l2 = len(s2)
        idx1 = 0
        idx2 = 0
        while idx1 < l1:
            if s1[idx1] == s2[idx2]:
                idx2 += 1
                if idx2 == l2:
                    start = idx1
                    end = idx1
                    idx2 -= 1
                    while idx2 >= 0:
                        if s2[idx2] == s1[start]:
                            idx2 -= 1
                        start -= 1
                    start += 1
                    currLength = end - start
                    if currLength < minSubLength:
                        minSubLength = currLength
                        minSubsequence = s1[start:end+1]
                    idx1 = start
            idx1 += 1

        return minSubsequence


s1 = "abcdebdde"
s2 = "bde"
print(Solution().minWindow(s1, s2))
s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
s2 = "u"
print(Solution().minWindow(s1, s2))
