# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        if veganFriendly == 1:
            restaurants = [id for id, _, veg, price, dis in sorted(
                restaurants, key=lambda x: (x[1], x[0]), reverse=True) if veg == 1 and price <= maxPrice and dis <= maxDistance]
        else:
            restaurants = [id for id, _, _, price, dis in sorted(
                restaurants, key=lambda x: (x[1], x[0]), reverse=True) if price <= maxPrice and dis <= maxDistance]

        return restaurants


restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
    3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10
print(Solution().filterRestaurants(
    restaurants, veganFriendly, maxPrice, maxDistance))
restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
    3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10
print(Solution().filterRestaurants(
    restaurants, veganFriendly, maxPrice, maxDistance))
restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
    3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 0
maxPrice = 30
maxDistance = 3
print(Solution().filterRestaurants(
    restaurants, veganFriendly, maxPrice, maxDistance))
