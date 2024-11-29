class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def match(a, b):
            ca, cb = ord(a)-ord('a'), ord(b)-ord('a')
            return ca == cb or (ca + 1) % 26 == cb
        j = 0
        for c in str1:
            if match(c, str2[j]): j += 1
            if j == len(str2): return True
        return False