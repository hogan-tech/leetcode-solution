from typing import Counter, List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Counter = Counter(arr1)
        result = []
        for item in arr2:
            while arr1Counter[item]:
                result.append(item)
                arr1Counter[item] -= 1
        tempList = []
        for item in arr1Counter.elements():
            while arr1Counter[item]:
                tempList.append(item)
                arr1Counter[item] -= 1
        tempList.sort()
        result.extend(tempList)
        return result


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]

print(Solution().relativeSortArray(arr1, arr2))
