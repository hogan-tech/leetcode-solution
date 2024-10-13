​# Python | SortedList | Sliding Window | O(nlogk) | O(k)

This Python script defines a class `Solution` that computes the x-sum of subarrays of a given length `k` from an array of integers `nums`. The x-sum is determined by counting the occurrences of elements and summing the top `x` most frequent elements.

## Time complexity: O(nlogk)
Frequency Count: SortedList will tak O(logk) duw to the binary search properties of SortedList.
Sliding Window: runs n - k time, time complexity is O((n - k)log(k))
## Space complexity: O(k)

### Imports
- **Counter**: A dictionary subclass from the `collections` module that counts the occurrences of elements in an iterable.
- **SortedList**: A data structure from the `sortedcontainers` module that maintains a sorted list for efficient insertions and deletions.
- **List**: Used for type hinting the list data type.

### Class Definition

```python
from collections import Counter
from sortedcontainers import SortedList
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        freq = Counter()
        freqCount = SortedList()  

        for i in range(k):
            num = nums[i]
            if num in freq:
                freqCount.remove((freq[num], num))
            freq[num] += 1
            freqCount.add((freq[num], num))
        
        def getTopXSum():
            tempSum = 0
            
            for count, num in freqCount[-x:]:
                tempSum += count * num
            return tempSum

        ans.append(getTopXSum())
        for i in range(k, n):
            oldNum = nums[i - k]
            newNum = nums[i]
            if freq[oldNum] > 0:
                freqCount.remove((freq[oldNum], oldNum))
                freq[oldNum] -= 1
                if freq[oldNum] > 0:
                    freqCount.add((freq[oldNum], oldNum))
                else:
                    del freq[oldNum]
            if newNum in freq:
                freqCount.remove((freq[newNum], newNum))
            freq[newNum] += 1
            freqCount.add((freq[newNum], newNum))

            ans.append(getTopXSum())

        return ans
```
