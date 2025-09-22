# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1
        result = []
        valueToSort = len(arr)
        while valueToSort > 0:
            index = arr.index(valueToSort)
            if index != valueToSort - 1:
                if index != 0:
                    result.append(index+1)
                    flip(arr, index+1)
                result.append(valueToSort)
                flip(arr, valueToSort)
            valueToSort -= 1
        return result


arr = [3, 2, 4, 1]
print(Solution().pancakeSort(arr))
arr = [1, 2, 3]
print(Solution().pancakeSort(arr))
