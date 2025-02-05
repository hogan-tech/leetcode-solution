from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        original = -1
        currCapacity = capacity
        move = 0
        for current in range(len(plants)):
            if currCapacity < plants[current]:
                currCapacity = capacity - plants[current]
                move = (current - original) * 2 - 1
                result += move
            else:
                move = 1
                result += 1
                currCapacity -= plants[current]
        return result


plants = [2, 2, 3, 3]
capacity = 5
print(Solution().wateringPlants(plants, capacity))
plants = [1, 1, 1, 4, 2, 3]
capacity = 4
print(Solution().wateringPlants(plants, capacity))
plants = [7, 7, 7, 7, 7, 7, 7]
capacity = 8
print(Solution().wateringPlants(plants, capacity))
plants = [3, 2, 4, 2, 1]
capacity = 6
print(Solution().wateringPlants(plants, capacity))
