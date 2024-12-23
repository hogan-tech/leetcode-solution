# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        total = 0
        freq = {}
        result = float("-inf")
        for right in range(len(fruits)):
            currFruit = fruits[right]
            if currFruit not in freq:
                freq[currFruit] = 1
            else:
                freq[currFruit] += 1
            total += 1
            while len(freq) > 2:
                prevFruit = fruits[left]
                freq[prevFruit] -= 1
                total -= 1
                left += 1
                if freq[prevFruit] == 0:
                    del freq[prevFruit]
            result = max(result, total)
        return result


fruits = [1, 2, 1]
print(Solution().totalFruit(fruits))
fruits = [0, 1, 2, 2]
print(Solution().totalFruit(fruits))
fruits = [1, 2, 3, 2, 2]
print(Solution().totalFruit(fruits))
fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(Solution().totalFruit(fruits))
