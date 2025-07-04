# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def kthCharacter(self, i: int, operations: List[int]) -> str:
        result = 0
        while i != 1:
            temp = i.bit_length() - 1
            if (1 << temp) == i:
                temp -= 1
            i -= 1 << temp
            if operations[temp]:
                result += 1
        return chr(ord("a") + (result % 26))

# word = a
# k = 1, k = 2
# gene b -> word ab
# k = 3, k = 4
# gene bc -> word abbc
# k = 5 -> k = 8
# gene bccd -> word abbcbccd
# k = 9 -> k = 16
# gene bccdcdde -> word abbcbccdbccdcdde


k = 5
operations = [0, 0, 0]
print(Solution().kthCharacter(k, operations))
k = 10
operations = [0, 1, 0, 1]
print(Solution().kthCharacter(k, operations))
