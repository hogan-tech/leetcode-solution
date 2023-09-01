from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(str(bin(i)).split("0b")[1].count('1'))
        return result
    
print(Solution().countBits(5))