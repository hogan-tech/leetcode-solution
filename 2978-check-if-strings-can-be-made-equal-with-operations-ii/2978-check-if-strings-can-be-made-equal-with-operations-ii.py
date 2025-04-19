class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1EvenFreq = [0] * 26
        s1OddFreq = [0] * 26
        s2EvenFreq = [0] * 26
        s2OddFreq = [0] * 26
        
        for i in range(len(s1)):
            cIdx = ord(s1[i]) - ord('a')
            if i % 2:
                s1OddFreq[cIdx] += 1
            else:
                s1EvenFreq[cIdx] += 1
        
        for i in range(len(s2)):
            cIdx = ord(s2[i]) - ord('a')
            if i % 2:
                s2OddFreq[cIdx] += 1
            else:
                s2EvenFreq[cIdx] += 1
        
        
        return s1OddFreq == s2OddFreq and s2EvenFreq == s1EvenFreq


s1 = "abcdba"
s2 = "cabdab"
print(Solution().checkStrings(s1, s2))
s1 = "abe"
s2 = "bea"
print(Solution().checkStrings(s1, s2))
