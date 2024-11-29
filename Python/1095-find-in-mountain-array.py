from typing import List


class MountainArray:
    def __init__(self, array: List[int]):
        self.array = array

    def get(self, index: int) -> int:
        if 0 <= index <= self.length():
            return self.array[index]
        return -1

    def length(self) -> int:
        return len(self.array)


class Solution:
    def findInMountainArray(self, target: int, mountainArray: 'MountainArray') -> int:
        length = mountainArray.length()

        low = 1
        high = length - 2
        while low != high:
            tempIndex = (low + high) // 2
            if mountainArray.get(tempIndex) < mountainArray.get(tempIndex + 1):
                low = tempIndex + 1
            else:
                high = tempIndex
        peakIndex = low

        low = 0
        high = peakIndex
        while low != high:
            tempIndex = (low + high) // 2
            if mountainArray.get(tempIndex) < target:
                low = tempIndex + 1
            else:
                high = tempIndex
        if mountainArray.get(low) == target:
            return low

        low = peakIndex + 1
        high = length - 1
        while low != high:
            tempIndex = (low + high) // 2
            if mountainArray.get(tempIndex) > target:
                low = tempIndex + 1
            else:
                high = tempIndex
        if mountainArray.get(low) == target:
            return low

        return -1


array = [0, 1, 2, 4, 2, 1]
target = 3

mountainArrayInstance = MountainArray(array)
print(Solution().findInMountainArray(target, mountainArrayInstance))
