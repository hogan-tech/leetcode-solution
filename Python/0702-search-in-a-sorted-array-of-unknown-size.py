# time complexity: O(logn)
# space complexity: O(1)
class ArrayReader:
    def get(self, index: int) -> int:
        return


class Solution:
    def search(self, reader: ArrayReader, target: int) -> int:
        if reader.get(0) == target:
            return 0
        left = 0
        right = 1
        while reader.get(right) <= target:
            left = right
            right <<= 1

        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            if num == target:
                return pivot
            if num < target:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1
