# time complexity: O(N + klogN)
# space complexity: O(N)
from heapq import heapify, heappop
from typing import Counter, List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        counterMap = Counter(words).items()
        for key, freq in counterMap:
            heap.append((-freq, key))
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(Solution().topKFrequent(words, k))
