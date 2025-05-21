from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result = set()
        if finalSum % 2:
            return []
        else:
            temp = 0
            i = 2
            while temp < finalSum:
                temp += i
                result.add(i)
                i += 2
            if temp != finalSum:
                result.remove(temp - finalSum)
            return list(result)


'''
6
1 2 3

14
1 2 3 4
1 2 3 4 5
'''
finalSum = 12
print(Solution().maximumEvenSplit(finalSum))
finalSum = 7
print(Solution().maximumEvenSplit(finalSum))
finalSum = 28
print(Solution().maximumEvenSplit(finalSum))
