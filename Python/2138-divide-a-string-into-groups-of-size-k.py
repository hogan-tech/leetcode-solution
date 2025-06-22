from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        while s:
            if len(s) >= k:
                result.append(s[:k])
            else:
                result.append(s + (fill * (k - len(s))))
            s = s[k:]
        return result


s = "abcdefghi"
k = 3
fill = "x"
print(Solution().divideString(s, k, fill))
s = "abcdefghij"
k = 3
fill = "x"
print(Solution().divideString(s, k, fill))
