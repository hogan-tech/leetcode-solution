# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ops = list(zip(indices, sources, targets))

        replaceMap = {}
        for i, src, tgt in sorted(ops, key=lambda x: x[0]):
            if s.startswith(src, i):
                if i not in replaceMap:
                    replaceMap[i] = (len(src), tgt)

        res = []
        i = 0
        while i < len(s):
            if i in replaceMap:
                src_len, tgt = replaceMap[i]
                res.append(tgt)
                i += src_len
            else:
                res.append(s[i])
                i += 1

        return ''.join(res)


s = "vmokgggqzp"
indices = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]
print(Solution().findReplaceString(s, indices, sources, targets))
s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
print(Solution().findReplaceString(s, indices, sources, targets))
s = "abcd"
indices = [0, 2]
sources = ["ab", "ec"]
targets = ["eee", "ffff"]
print(Solution().findReplaceString(s, indices, sources, targets))
