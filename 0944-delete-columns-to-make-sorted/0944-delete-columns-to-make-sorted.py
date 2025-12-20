# time complexity: O(n*k)
# space complexity: O(1)
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        sLen = len(strs[0])
        result = 0
        for i in range(sLen):
            temp = ""
            for s in strs:
                temp = temp + s[i]
            if temp != "".join(sorted(temp)):
                result += 1
        return result


'''
c b a
d a f
g h i
'''
strs = ["cba", "daf", "ghi"]
print(Solution().minDeletionSize(strs))
strs = ["a", "b"]
print(Solution().minDeletionSize(strs))
strs = ["zyx", "wvu", "tsr"]
print(Solution().minDeletionSize(strs))
