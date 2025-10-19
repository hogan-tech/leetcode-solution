from heapq import heapify, heappop, heappush
from math import sqrt
from typing import List

# time complexity: O(nlogk)
# space complexity: O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHp = [(-(x ** 2 + y ** 2), x, y) for x, y in points[:k]]
        heapify(maxHp)
        for currX, currY in points[k:]:
            dist = -(currX ** 2 + currY ** 2)
            if dist > maxHp[0][0]:
                heappop(maxHp)
                heappush(maxHp, (dist, currX, currY))

        return [[x, y] for _, x, y in maxHp]

# time complexity: O(nlogn)
# space complexity: O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(sqrt(x**2 + y**2), x, y) for x, y in points]
        heapify(minHeap)
        result = []
        while k:
            _, currX, currY = heappop(minHeap)
            result.append([currX, currY])
            k -= 1
        return result
    
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [self.distance(point) for point in points]
        remaining = [i for i in range(len(points))]
        left, right = 0, max(distances)
        
        closest = []
        while k:
            mid = (left + right) // 2
            closer, farther = self.splitDis(remaining, distances, mid)
            if len(closer) > k:
                remaining = closer
                right = mid
            else:
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                left = mid
        return [points[i] for i in closest]

    def splitDis(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def distance(self, point: List[int]) -> float:
        return point[0] ** 2 + point[1] ** 2

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSelect(points, k)
    
    def quickSelect(self, points: List[List[int]], k: int) -> List[List[int]]:
        left, right = 0, len(points) - 1
        pivotIdx = len(points)
        while pivotIdx != k:
            pivotIdx = self.partition(points, left, right)
            if pivotIdx < k:
                left = pivotIdx
            else:
                right = pivotIdx - 1
        
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        pivot = self.choosePivot(points, left, right)
        pivotDis = self.distance(pivot)
        while left < right:
            if self.distance(points[left]) >= pivotDis:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        if self.distance(points[left]) < pivotDis:
            left += 1
        return left
    
    def choosePivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
        return points[left + (right - left) // 2]
    
    def distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2

points = [[1, 3], [-2, 2]]
k = 1
print(Solution().kClosest(points, k))
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(Solution().kClosest(points, k))
