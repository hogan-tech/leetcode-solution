# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.dict = defaultdict(list)
        for i, num in enumerate(nums):
            self.dict[num].append(i)

    def pick(self, target: int) -> int:
        targetList = self.dict[target]
        randomNum = random.randint(0, len(targetList)-1)
        return targetList[randomNum]


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 3, 3])
print(obj.pick(3))
print(obj.pick(1))
print(obj.pick(3))
print(obj.pick(2))
print(obj.pick(3))
print(obj.pick(3))
print(obj.pick(3))
