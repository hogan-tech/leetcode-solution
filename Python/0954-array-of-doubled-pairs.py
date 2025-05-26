# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for key in sorted(arr, key=abs):
            if counter[key] == 0:
                continue
            if counter[2 * key] == 0:
                return False
            counter[key] -= 1
            counter[2*key] -= 1
        return True


'''
x, 2x, 4x, 8x ...
y, 2y, 4y, 8y ...

[x, 2x, 4x, 8x, y, 2y, 4y, 8y]


3 ->  0011
6 ->  0110
12 -> 1100



'''
arr = [3, 1, 3, 6]
print(Solution().canReorderDoubled(arr))
arr = [2, 1, 2, 6]
print(Solution().canReorderDoubled(arr))
arr = [4, -2, 2, -4]
print(Solution().canReorderDoubled(arr))
