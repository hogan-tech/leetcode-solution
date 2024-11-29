from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        convertNumber = int(''.join(str(item) for item in digits))+1
        convertList = list(str(convertNumber))
        return [int(i) for i in convertList]


digits = [9, 9, 9, 9]
print(Solution().plusOne(digits))
