# time complexity: O(n+m+q1​+q2*n)
# space complexity: O(n+m)
from typing import Counter, List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:

        self.counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter[self.nums2[index]] += 1

    def count(self, total: int) -> int:

        result = 0
        for num in self.nums1:
            if (rest := total - num) in self.counter:
                result += self.counter[rest]
        return result


findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(findSumPairs.count(7))
findSumPairs.add(3, 2)
print(findSumPairs.count(8))
print(findSumPairs.count(4))
findSumPairs.add(0, 1)
findSumPairs.add(1, 1)
print(findSumPairs.count(7))
