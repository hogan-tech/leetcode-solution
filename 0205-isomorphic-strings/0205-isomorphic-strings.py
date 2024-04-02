# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappingST, mappingTS = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 not in mappingST) and (c2 not in mappingTS):
                mappingST[c1] = c2
                mappingTS[c2] = c1
            elif mappingST.get(c1) != c2 or mappingTS.get(c2) != c1:
                return False
        return True


s = "egf"
t = "add"

print(Solution().isIsomorphic(s, t))
