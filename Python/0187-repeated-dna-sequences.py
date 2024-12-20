# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        visited = set()
        currString = s[:10]
        visited.add(currString)
        for i in range(1, len(s) - 9):
            currString = currString[1:] + s[i+9]
            if currString in visited:
                result.add(currString)
            else:
                visited.add(currString)
        return list(result)


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(Solution().findRepeatedDnaSequences(s))
s = "AAAAAAAAAAAAA"
print(Solution().findRepeatedDnaSequences(s))
s = "AAAAAAAAAAA"
print(Solution().findRepeatedDnaSequences(s))
