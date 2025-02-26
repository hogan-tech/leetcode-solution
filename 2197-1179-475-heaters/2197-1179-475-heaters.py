# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        distances = []
        for house in houses:
            heaterIdx = min(binarySearch(heaters, house), len(heaters) - 1)
            minDis = min(
                abs(house - heaters[heaterIdx]), abs(house - heaters[heaterIdx - 1]))
            distances.append(minDis)
        return max(distances)


houses = [1, 2, 3]
heaters = [2]
print(Solution().findRadius(houses, heaters))
houses = [1, 2, 3, 4]
heaters = [1, 4]
print(Solution().findRadius(houses, heaters))
houses = [1, 5]
heaters = [2]
print(Solution().findRadius(houses, heaters))

'''
house to every heater min distance
radius = min of whole distances
1 2 3
  2
  
1 2 3 4
1     4

1       5
  2 
'''
