import heapq
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        peopleSorted = sorted(people)
        dic = {}
        heap = []
        i = 0
        for person in peopleSorted:
            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap, flowers[i][1])
                i += 1
            while heap and heap[0] < person:
                heapq.heappop(heap)

            dic[person] = len(heap)

        return [dic[x] for x in people]


flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
people = [2, 3, 7, 11]

print(Solution().fullBloomFlowers(flowers, people))
