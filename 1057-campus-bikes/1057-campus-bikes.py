# n workers & m bikes
# time complexity: nmO(nm)
# space complexity: O(nm)

from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        def find_distance(workerLoc, bikeLoc):
            return abs(workerLoc[0] - bikeLoc[0]) + abs(workerLoc[1] - bikeLoc[1])

        allTriplets = []
        for worker, workerLoc in enumerate(workers):
            for bike, bikeLoc in enumerate(bikes):
                distance = find_distance(workerLoc, bikeLoc)
                allTriplets.append((distance, worker, bike))

        allTriplets.sort()

        bikeStatus = [False] * len(bikes)
        workerStatus = [-1] * len(workers)
        pairCount = 0

        for distance, worker, bike in allTriplets:
            if workerStatus[worker] == -1 and not bikeStatus[bike]:
                bikeStatus[bike] = True
                workerStatus[worker] = bike
                pairCount += 1

                if pairCount == len(workers):
                    return workerStatus

        return workerStatus


workers = [[0, 0], [2, 1]]
bikes = [[1, 2], [3, 3]]

print(Solution().assignBikes(workers, bikes))
